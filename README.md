# git_test
Các bạn hãy làm theo chỉ dẫn của [bài tập 1](exercise_1/README.md) để làm quen với các lệnh cơ bản trong Git.

Cách sử dụng của một số lệnh:
- `git clone [url]`: Tải một repo xuống, url có dạng github.com/[author]/[project-name.git], ví dụ https://github.com/masspvn/pre-program-package.git. Ngoài ra cũng có thể tải repo xuống dưới dạng zip.
- `git log`: xem lịch sử các commit
- `git blame file1`: xem lịch sử thay đổi của file1
- `git status`: List ra toàn bộ các file mới hoặc bị thay đổi
- `git add file1 file2`: file1 và file2 là 2 files mới hoặc mới bị thay đổi, dùng lệnh này để đưa 2 files này vào staging area, chuẩn bị commit
- `git add /path/to/*`: đưa tất cả các file trong thư mục /path/to/ vào staging area
- `git commit -m \"Some meaningful message about this commit\"`: Lưu lại các file trong staging area vào một commit với chú thích "Some meaningful message about this commit" . Chú ý commit message cần ngắn gọn, dễ hiểu, tóm tắt lại những thay đổi của version này so với version trước
- `git pull`: Tải về những thay đổi mới những người khác đã commit vào nhánh hiện tại, thường là <i>master</i> - tên nhánh chính của repo
- `git push`: Đưa thay đổi của những local commit lên nhánh hiện tại của repo trên Github - khi người khác dùng lệnh git pull trên ở cùng nhánh, họ sẽ thấy những thay đổi này
- `git checkout -b new_branch_name`: tạo một nhánh mới <i>new_branch_name</i>
- `git checkout branch_name`: di chuyển giữa các nhánh trên máy tính
