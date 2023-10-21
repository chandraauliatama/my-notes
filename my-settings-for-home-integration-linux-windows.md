# What Is This?

Tulisan ini berisi bagaimana saya mengintegrasikan penyimpanan/storage perangkat saya agar antara windows dan linux bisa mengakses file yang sama.

## Informasi

OS: Windows 11 & PopOS
Daftar Partisi:

- C: (Windows System)
- D: Tempat Utama File (Wajib NTFS)
- E: (Home Linux, bisa digabung dengan / atau hanya /home)

## Langkah Langkah

1. Pada Windows biasamya ada folder-folder default seperti: Downloads, Documents, Pictures, Videos, Music.

   - Silakan move lokasi folder-folder ini melalui properties folder(bukan move bisa dengan ctrl+x lalu ctrl+p).
   - File dan folder yang ingin diakses oleh linux dan windows pastikan berada di partisi D.

2. Pada linux, mount partisi D secara dafault dan otomatis dengan cara berikut

   - Buka terminal dan buka file fstab
     ```
     sudo nvim /etc/fstab
     ```
   - Tambahkan baris berikut:
     ```
     /dev/disk/by-uuid/714F3AA13A97DA0D /mnt/D auto nosuid,nodev,nofail,x-gvfs-show,x-gvfs-name=Local%20Data,x-gvfs-icon=Local%20Data,x-gvfs-symbolic-icon=Local%20Data,uid=1000 0 0
     ```
   - Perhatikan string **714F3AA13A97DA0D** ini merupakan UUID dari partisi D, cara cek menggunakan aplikasi **gnome-disks-utility**
   - Perhatikan string **/mnt/D** ini merupakan cara kita merefer dimana kita akan membacanya pada linux, diperlukan ketika membuat link nanti
   - Simpan file yang sudah ditambahkan baris tersebut

3. Buat links antara linux dengan window
   - Contoh pada folder Downloads
   - hapus folder Downloads default pada home linux
     ```
     rm -rf ~/Downloads
     ```
   - buat links dengan partisi D tadi
     ```
     ln -s /mnt/D/Downloads ~/Downloads
     ```
