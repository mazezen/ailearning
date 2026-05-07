#!/use/bin/python3

import os, sys, stat

# 获取当前的工作目录
current_dir = os.getcwd()
print(current_dir)

# 改变当前的工作目录
# os.chdir("../")
# current_dir = os.getcwd()
# print(current_dir)

# 列出目录内容
files_and_dirs = os.listdir()
print(files_and_dirs)

# 创建目录
os.mkdir("new_directory")

# 删除目录
os.rmdir("new_directory")

# 删除文件
# os.remove("file_to_delete.txt")

# 重命名文件或者目录
# os.rename("old_name.txt", "new_name.txt")

# 执行系统命令
print(os.system("ls -l"))


'''
    os.access(path, mode)

    mode:
        os.F_OK: 作为access()的mode参数，测试path是否存在。
        os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
        os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
        os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
'''
ret = os.access("/tmp/foo.txt", os.F_OK)
print("F - OK 返回值 %s" % ret)

ret = os.access("/tmp/foo.txt", os.R_OK)
print("R - OK 返回值 %s" % ret)

ret = os.access("/tmp/foo.txt", os.W_OK)
print("W - OK 返回值 %s" % ret)

ret = os.access("/tmp/foo.txt", os.X_OK)
print("x - OK 返回值 %s" % ret)


'''
os.chflags(path, flags)

path -- 文件名路径或目录路径。

flags -- 可以是以下值：
    · stat.UF_NODUMP: 非转储文件
    · stat.UF_IMMUTABLE: 文件是只读的
    · stat.UF_APPEND: 文件只能追加内容
    · stat.UF_NOUNLINK: 文件不可删除
    · stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
    · stat.SF_ARCHIVED: 可存档文件(超级用户可设)
    · stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
    · stat.SF_APPEND: 文件只能追加内容(超级用户可设)
    · stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
    · stat.SF_SNAPSHOT: 快照文件(超级用户可设)
'''

path = "/tmp/foo.txt"

# flags = stat.SF_NOUNLINK
# flags = stat.UF_NODUMP
# flags = stat.SF_IMMUTABLE
flags = stat.UF_APPEND
retval = os.chflags( path, flags )
print("返回值: %s" % retval)
