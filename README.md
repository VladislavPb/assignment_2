# assignment_2
Job test for junior developer vacancy

Задача:

Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы, вычисленные по соответствующему алгоритму и указанные в файле через пробел. Напишите программу, читающую данный файл и проверяющую целостность файлов.


Пример файла с чек-суммами:

file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906

file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e

file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e

file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709

Пример вызова:  
your_program   path_to_the_input_file   path_to_the_directory_containing_the_files_to_check

  
Формат вывода:
  
file_01.bin OK
  
file_02.bin FAIL
  
file_03.bin NOT FOUND
  
file_04.txt OK
