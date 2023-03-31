# Лабораторная работа №1: [C++ & UNIX]: UNIX знакомство: useradd, nano, chmod, docker, GIT, CI, CD #
Хрусталев И. Д., ФФ ИТМО, Z33434

## Цель
Познакомить студента с основами администрирования программных комплексов в ОС
семейства UNIX, продемонстрировать особенности виртуализации и контейнеризации,
продемонстрировать преимущества использования систем контроля версий (на
примере GIT)

## Отчет о выполнении

1. [ОС] Работа в ОС, использование файловой системы, прав доступа, исполение файлов

    1. В папке /USR/LOCAL/ создать 2 директории: folder_max, folder_min
    ```
    dimasik@DESKTOP-KTOS6NV:~$ cd /usr/local
    dimasik@DESKTOP-KTOS6NV:/usr/local$ mkdir folder_max
    dimasik@DESKTOP-KTOS6NV:/usr/local$ mkdir folder_max
    
    ```
    
    
    2. Создать 2-х группы пользователей: group_max, group_min
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local sudo groupadd group_max
    dimasik@DESKTOP-KTOS6NV:/usr/local$ sudo groupadd group_min
    
    ```
    3. Создать 2-х пользователей: user_max_1, user_min_1
    ```
    khrstln@LinuxUbuntu:/usr/local$ sudo useradd user_max_1
    khrstln@LinuxUbuntu:/usr/local$ sudo useradd user_min_1
    
    khrstln@LinuxUbuntu:/usr/local$ members group_max
    user_max_1
    
    khrstln@LinuxUbuntu:/usr/local$ members group_min
    user_min_1
    ```
    4. Для пользователей из группы *_max дать полный доступ на директории *_max и *_min. Для пользователей группы *_min дать полный доступ только на директорию *_min
    ```
    khrstln@LinuxUbuntu:/usr/local$ sudo chmod a=rwx folder_min
    khrstln@LinuxUbuntu:/usr/local$ sudo chmod o-w folder_max
    
    khrstln@LinuxUbuntu:/usr/local$ ls -l
    ...
    drwxrwxr-x 2 root    group_max  4096 мар 12 22:17 folder_max
    drwxrwxrwx 2 root    group_min  4096 мар 12 22:19 folder_min
    ...
    ```


    5. Создать и исполнить (пользователем из той же категории) скрипт в директории folder_max, который пишет текущую дату/время в файл output.log в текущей директории
    ```
    khrstln@LinuxUbuntu:/usr/local/folder_max$ su - user_max_1
    $ whoami
    user_max_1
    $ touch date.sh
    ```
    
    После создания файла в директории folder_max открываем его с помощью команды 
    ```
    $ nano date.sh
    ```
    
    Пишем в файл следующий скрипт
    ```
    #!/bin/bash
    date  >> /usr/local/folder_max/output.log
    ```
    
      Чтобы исполнить файл, в терминале пишем следующие команды
    ```
    $ chmod g=rwx date.sh
    $ ./date.sh
    ```

    6. Создать и исполнить (пользователем из той же категории) скрипт в директории folder_max, который пишет текущую дату/время в файл output.log в директории *_min
    ```
    $ touch date_in_min.sh
    ```
    
    После создания файла в директории folder_max открываем его с помощью команды 
    ```
    $ nano date_in_min.sh
    ```
    
    Пишем в файл следующий скрипт
    ```
    #!/bin/bash
    date  >> /usr/local/folder_min/output_from_max.log
    ```
    
    Чтобы исполнить файл, в терминале пишем следующие команды
    ```
    $ chmod a=rwx date_in_min.sh
    $ bash date_in_min.sh
    ```


    7. Исполнить (пользователем *_min) скрипт в директории folder_max, который пишет текущую дату/время в файл output.log в директории *_min
    ```
    $ whoami
    user_min_1
    $ pwd
    /usr/local/folder_max
    $ bash date_in_min.sh
    ```


    8. Создать и исполнить (пользователем из той же категории) скрипт в директории folder_min, который пишет текущую дату/время в файл output.log в директории *_max
    ```
    $ cd ..
    $ cd folder_min
    $ pwd
    /usr/local/folder_min
    $ touch date_in_max.sh
    ```
    
    После создания файла в директории folder_max открываем его с помощью команды 
    ```
    $ nano date_in_max.sh
    ```
    
    Пишем в файл следующий скрипт
    ```
    #!/bin/bash
    date  >> /usr/local/folder_max/output_from_min.log
    ```
    
    Чтобы исполнить файл, в терминале пишем следующие команды
    ```
    $ chmod a=rwx date_in_min.sh
    $ bash date_in_min.sh
    ```
    


    9. Вывести перечень прав доступа у папок *_min/ *_max, а также у всего содержимого внутри
    ```
    khrstln@LinuxUbuntu:/usr/local$ ls -l
    drwxrwxr-x 2 root    group_max  4096 мар 23 17:27 folder_max
    drwxrwxrwx 2 root    group_min  4096 мар 23 18:02 folder_min
    ```

2. [КОНТЕЙНЕР] docker build / run / ps / images
    1. Создать скрипт, который пишет текущую дату/время в файл output.log в текущей директории
    
    Будем работать в директории /usr/local. Создадим файл date.sh со следующим содержанием
    
    ```
    #!/bin/bash
    date >> output.log
    ```
    
    2. Собрать образ со скриптами выше и с пакетом nano (docker build)
    ```
    khrstln@LinuxUbuntu:/usr/local$ sudo docker image build -t myimage .
    
    khrstln@LinuxUbuntu:/usr/local$ sudo docker image ls
    myimage       latest    a54a4e4feccf   45 minutes ago   121MB
    ```
    3. Запустить образ (docker run)
    ```
    khrstln@LinuxUbuntu:/usr/local$ sudo docker run -it myimage
    root@4829ba9bd0e0:/#
    ```
    
    4. Выполнить скрипт, который подложили при сборке образа
    ```
    root@4829ba9bd0e0:/# ls
    bin      dev   lib    libx32  opt   run   sys  var
    boot     etc   lib32  media   proc  sbin  tmp
    date.sh  home  lib64  mnt     root  srv   usr
    root@4829ba9bd0e0:/# ./date.sh
    Fri Mar 24 12:40:26 UTC 2023
    ```
    
    5.	Вывести список пользователей в собранном образе
    ```
    khrstln@LinuxUbuntu:/usr/local$ sudo docker run myimage id
    uid=0(root) gid=0(root) groups=0(root) 
    ```

3. [GIT] GitHub / GitLab, в котором будут содержаться все выполненные ЛР
    1. Создать репозиторий в GitHub или GitLab
    ```
    khrstln@LinuxUbuntu:/usr/local$ apt install git
    khrstln@LinuxUbuntu:/usr/local$ git config --global user.name khrstln
    khrstln@LinuxUbuntu:/usr/local$ git config --global user.email iliss002@mail.ru
    ```
    Дальнейшие команды выполняются после добавления в Cpp_and_unix всех необходимых папок и файлов
    ```
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git init
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git add .
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git commit -m 'Final version'
    ```
    
    2. Создать структуру репозитория
    ```
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ mkdir lab_1
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ cd lab_1
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix/lab_1$ mkdir build
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix/lab_1$ mkdir doc
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix/lab_1$ mkdir src
    ```
    Далее скопируем директории folder_max и folder_min в lab_1
    
    3. Создать ветки dev / stg / prd, удалить ранее существующие ветки удаленно и локально
    Создадим фиктивную ветку fake
    ```
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git branch fake
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git branch
      fake
    * main
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git push origin fake
    ```
    Создадим ветки dev, stg, prd
    ```
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git branch dev
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git branch stg
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git branch prd
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git branch
      dev
      stg
      prd
      fake
    * main
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git push origin dev
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git push origin stg
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git push origin prd
    ```
    Удалим ветку fake локально и удаленно
    ```
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git branch -d fake
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git branch
      dev
      stg
      prd
    * main
    khrstln@LinuxUbuntu:/usr/local/Cpp_and_unix$ git push origin :fake
    To github.com:khrstln/Cpp_and_unix.git
    - [deleted]         fake
    ```

    4. Создать скрипт автоматического переноса ревизий из ветки dev в ветку stg с установкой метки времени (tag). Скрипт в корень репозитория
    
    Создадим в директории lab_1 файл from_dev_to_stg.sh и запишем в него следующий скрипт
    ```
    #!/bin/bash
    git checkout stg
    git merge --commit dev
    time_tag=$(date '+%d.%m.%Y.%H.%M.%S')
    git tag "$time_tag"
    git push origin stg
    git push origin "$time_tag"
    ```
    5. Создать скрипт автоматического переноса ревизий из ветки stg в ветку prd с установкой метки времени (tag). Скрипт в корень репозитория
    
    Создадим в директории lab_1 файл from_stg_to_prd.sh и запишем в него следующий скрипт
    ```
    #!/bin/bash
    git checkout prd
    git merge --commit dev
    time_tag=$(date '+%d.%m.%Y.%H.%M.%S')
    git tag "$time_tag"
    git push origin prd
    git push origin "$time_tag"
    ```

Дополнительные вопросы
Чем контейнер отличается от образа?









    
