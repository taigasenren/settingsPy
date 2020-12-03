#現在いるディレクトリをzipファイル化するシステム
import os
import shutil

os.chdir('../')
cd = os.getcwd()
print(shutil.make_archive(cd, 'zip', root_dir = cd))