# Cara Menghubungkan Sistem Operasi dengan Github via SSH

## Perhatikan
- Git sudah terinstall
- ssh sudah terinstal
- cara ini digunakan pada sistem operasi berbasis debian

## langkah-langkah
1. Setting git username dan email
```
git config --global user.name "chandraauliatama" 

git config --global user.email "your@email.com" 
```
2. Generate ssh key baru pada terminal
```
ssh-keygen -t ed25519 -C "your_email@gmail.com"
```
3. Masuk ke direktori ssh
```
cd ~/.ssh
```
4. Cek file dengan ekstensi .pub
5. Tampilkan isi dari file tersebut, sebagai contoh
```
cat id_ed32424.pub
```
6. Hasil output dari cat tersebut silakan copy dan paste pada (link berikut https://github.com/settings/ssh/new)[https://github.com/settings/ssh/new]
7. cek status koneksi
```
ssh -T git@github.com
```
8. Bila berhasil akan muncul
```
Hi chandraauliatama! You've successfully authenticated, but GitHub does not provide shell access.
```


