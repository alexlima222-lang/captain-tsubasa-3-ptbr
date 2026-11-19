"""Aplica a candidata PT-BR 356 à ROM japonesa verificada. Python 3, sem dependências."""
from pathlib import Path
import argparse,hashlib,sys
ORIGINAL_SHA256='6a299b99e0a55aec6669930dc622037d82d297e875630273c6cd6f05438aa3e6'
TARGET_SHA256='b302f1f3268da2ed2887b3eff5b532f8794fc678b9af42dc1110a04d16213a8c'
PATCH_SHA256='46d2d6de9d8520793ebefee5d328bca89d84246c4cf3d74e20c4659d0c0dff0d'
def sha(data):return hashlib.sha256(data).hexdigest()
def apply(original,patch):
 if len(original)==1049088:original=original[512:]
 if sha(original)!=ORIGINAL_SHA256:raise ValueError('ROM de origem incompatível. Use a japonesa original indicada no LEIA-ME.')
 if sha(patch)!=PATCH_SHA256:raise ValueError('Patch incompatível ou danificado.')
 if patch[:5]!=b'PATCH':raise ValueError('Cabeçalho IPS inválido.')
 out=bytearray(original);i=5
 while True:
  if i+3>len(patch):raise ValueError('Patch truncado.')
  if patch[i:i+3]==b'EOF':
   if i+3!=len(patch):raise ValueError('Dados inesperados após EOF.')
   break
  if i+5>len(patch):raise ValueError('Registro IPS truncado.')
  at=int.from_bytes(patch[i:i+3],'big');n=int.from_bytes(patch[i+3:i+5],'big');i+=5
  if n:
   if i+n>len(patch):raise ValueError('Dados IPS truncados.')
   data=patch[i:i+n];i+=n
  else:
   if i+3>len(patch):raise ValueError('RLE truncado.')
   n=int.from_bytes(patch[i:i+2],'big');data=patch[i+2:i+3]*n;i+=3
  if at+n>2097152:raise ValueError('Registro além do tamanho permitido.')
  if len(out)<at+n:out.extend(bytes(at+n-len(out)))
  out[at:at+n]=data
 if len(out)!=2097152 or sha(out)!=TARGET_SHA256:raise ValueError('Verificação da ROM resultante falhou.')
 return bytes(out)
def main(argv=None):
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('rom',type=Path);parser.add_argument('--patch',type=Path,default=Path(__file__).with_name('CT3_356_PTBR_LOGOTIPO.ips'));parser.add_argument('--output',type=Path);args=parser.parse_args(argv)
 try:
  data=apply(args.rom.read_bytes(),args.patch.read_bytes());output=args.output or args.rom.with_name('CT3_356_PTBR_LOGOTIPO.sfc')
  if output.exists():
   if sha(output.read_bytes())==TARGET_SHA256:print('Candidata já verificada:',output);return 0
   raise ValueError('O arquivo de destino já existe e será preservado. Escolha outro --output.')
  with output.open('xb')as f:f.write(data)
  print('Candidata criada e verificada:',output);print('SHA-256:',TARGET_SHA256);return 0
 except (OSError,ValueError)as e:print('Erro:',e,file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
