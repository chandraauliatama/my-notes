# How I Sync or Backup My Computer Data to Google Drive

## Requirement

1. Rclone
    ```bash
    sudo -v ; curl https://rclone.org/install.sh | sudo bash
    ```

## Command
1. Backup to gdrive:
    ```
    alias backupkuliah="rclone copy /mnt/D/Kuliah chandraaulia444:/kuliah -P"
    ```

2. Get all data to local
    ```
    alias synclocalkuliah="rclone sync chandraaulia444:/kuliah /mnt/D/Kuliah -P --drive-acknowledge-abuse"
    ```

## References
1. [Back Up Your Google Drive Files with Rclone](https://dmuth.medium.com/back-up-your-google-drive-files-with-rclone-ff8ff6682db)
2. [Internet Archive](https://web.archive.org/web/20230521034801/https://dmuth.medium.com/back-up-your-google-drive-files-with-rclone-ff8ff6682db)
3. 


