"""
OS module : to aotumate operating system operation like folder manipulation
DirEntry
EX_OK
F_OK
GenericAlias
Mapping
MutableMapping
O_APPEND
O_BINARY
O_CREAT
O_EXCL
O_NOINHERIT
O_RANDOM
O_RDONLY
O_RDWR
O_SEQUENTIAL
O_SHORT_LIVED
O_TEMPORARY
O_TEXT
O_TRUNC
O_WRONLY
P_DETACH
P_NOWAIT
P_NOWAITO
P_OVERLAY
P_WAIT
PathLike
R_OK
SEEK_CUR
SEEK_END
SEEK_SET
TMP_MAX
W_OK
X_OK
_AddedDllDirectory
_Environ
__all__
__builtins__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_check_methods
_execvpe
_exists
_exit
_fspath
_get_exports_list
_walk
_wrap_close
abc
abort
access
add_dll_directory
altsep
chdir
chmod
close
closerange
cpu_count
curdir
defpath
device_encoding
devnull
dup
dup2
environ
error
execl
execle
execlp
execlpe
execv
execve
execvp
execvpe
extsep
fdopen
fsdecode
fsencode
fspath
fstat
fsync
ftruncate
get_exec_path
get_handle_inheritable
get_inheritable
get_terminal_size
getcwd
getcwdb
getenv
getlogin
getpid
getppid
isatty
kill
linesep
link
listdir
lseek
lstat
makedirs
mkdir
name
open
pardir
path
pathsep
pipe
popen
putenv
read
readlink
remove
removedirs
rename
renames
replace
rmdir
scandir
sep
set_handle_inheritable
set_inheritable
spawnl
spawnle
spawnv
spawnve
st
startfile
stat
stat_result
statvfs_result
strerror
supports_bytes_environ
supports_dir_fd
supports_effective_ids
supports_fd
supports_follow_symlinks
symlink
sys
system
terminal_size
times
times_result
truncate
umask
uname_result
unlink
unsetenv
urandom
utime
waitpid
waitstatus_to_exitcode
walk
write

"""
import os



#this will display all item inside os module
# lst=list(dir(os))
# for i in lst:
#     print(i)


#make directory: create directory in current workspace
#here i used condition to check whether file exists or not if not create file if yes ignore code
# if(not os.path.exists("Data")):
#     os.mkdir("data")
#     for i in range(0,10):
#         os.mkdir(f"data/day{i+1}")



#to rename files
# for i in range(0,10):
#     #os.rename(source - kispe karna hai ,destination - kya karna hai)
#     os.rename(f"data/day{i+1}", f"data/tutorial {i+1}")


#item list inside directory
folders= os.listdir("data")
# print(folders)
for i in folders:
    print(i)


#item list inside directory of directory -this will print inside directory / directory
for i in folders:
    print(os.listdir(f"data/{i}"))


#system used to open and run specific file
print(os.system("1.FIRST.py"))


#delete a file
print(os.remove("tempCodeRunnerFile.py"))