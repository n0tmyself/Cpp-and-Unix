# Лабораторная работа №1: [C++ & UNIX]: UNIX знакомство: useradd, nano, chmod, docker, GIT, CI, CD #
Альшевский Д.В., ФФ ИТМО, Z33434

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
    dimasik@DESKTOP-KTOS6NV:/usr/local$ sudo useradd user_max_1
    dimasik@DESKTOP-KTOS6NV:/usr/local$ sudo useradd user_min_1
    
    ```
    4. Для пользователей из группы *_max дать полный доступ на директории *_max и *_min. Для пользователей группы *_min дать полный доступ только на директорию *_min
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local$ sudo chmod a=rwx folder_min
    dimasik@DESKTOP-KTOS6NV:/usr/local$ sudo chmod o-wx folder_max
    
    dimasik@DESKTOP-KTOS6NV:/usr/local$ ls -l
    ...
    drwxrwxr-- 2 root    group_max  4096 мар 12 22:17 folder_max
    drwxrwxrwx 2 root    group_min  4096 мар 12 22:19 folder_min
    ...
    ```


    5. Создать и исполнить (пользователем из той же категории) скрипт в директории folder_max, который пишет текущую дату/время в файл output.log в текущей директории
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local/folder_max$ su - user_max_1
    $ whoami
    user_max_1
    $ touch script_max
    ```
    
    После создания файла в директории folder_max открываем его с помощью команды 
    ```
    $ nano script_max
    ```
    
    Пишем в файл следующий скрипт
    ```
    #!/bin/bash
    date | tee output.log
    ```
    
      Чтобы исполнить файл, в терминале пишем следующие команды
    ```
    $ chmod g=rwx script_max
    $ ./script_max
    ```

    6. Создать и исполнить (пользователем из той же категории) скрипт в директории folder_max, который пишет текущую дату/время в файл output.log в директории *_min
    ```
    $ touch script_min
    ```
    
    После создания файла в директории folder_max открываем его с помощью команды 
    ```
    $ nano script_min
    ```
    
    Пишем в файл следующий скрипт
    ```
    #!/bin/bash
    date | tee /usr/local/folder_min/output.log
    ```
    
    Чтобы исполнить файл, в терминале пишем следующие команды
    ```
    $ chmod a=rwx script_min
    $ bash script_min
    ```


    7. Исполнить (пользователем *_min) скрипт в директории folder_max, который пишет текущую дату/время в файл output.log в директории *_min
    ```
    $ whoami
    user_min_1
    $ pwd
    /usr/local/folder_max
    $ bash script_min
    ```


    8. Создать и исполнить (пользователем из той же категории) скрипт в директории folder_min, который пишет текущую дату/время в файл output.log в директории *_max
    ```
    $ cd ..
    $ cd folder_min
    $ pwd
    /usr/local/folder_min
    $ touch script_min
    ```
    
    После создания файла в директории folder_max открываем его с помощью команды 
    ```
    $ nano script_min
    ```
    
    Пишем в файл следующий скрипт
    ```
    #!/bin/bash
    date | tee /usr/local/folder_max/output_min.log
    ```
    
    Чтобы исполнить файл, в терминале пишем следующие команды
    ```
    $ chmod a=rwx script_min
    $ bash script_min
    ```
    


    9. Вывести перечень прав доступа у папок *_min/ *_max, а также у всего содержимого внутри
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local$ ls -l
    drwxrwx--- 2 user_max_1 group_max 4096 Mar 31 21:57 folder_max
    drwxrwxrwx 2 user_min_1 group_min 4096 Mar 31 21:59 folder_min
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
    dimasik@DESKTOP-KTOS6NV:/usr/local$ sudo docker image build -t myimage .
    
    dimasik@DESKTOP-KTOS6NV:/usr/local$ sudo docker image ls
    myimage       latest    a54a4e4feccf   45 minutes ago   121MB
    ```
    3. Запустить образ (docker run)
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local$ sudo docker run -it myimage
   dimasik@DESKTOP-KTOS6NV:/#
    ```
    
    4. Выполнить скрипт, который подложили при сборке образа
    ```
    dimasik@DESKTOP-KTOS6NV:/# ls
    bin   date.sh  etc   lib    lib64   media  opt         proc  run   srv  tmp  var
    boot  dev      home  lib32  libx32  mnt    output.log  root  sbin  sys  usr
    dimasik@DESKTOP-KTOS6NV:/# bash date.sh
    Fri Mar 31 19:35:33 UTC 2023
    dimasik@DESKTOP-KTOS6NV:/#
    ```
    
    5.	Вывести список пользователей в собранном образе
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local$ docker run mydocker id
    uid=0(root) gid=0(root) groups=0(root)
    ```

3. [GIT] GitHub / GitLab, в котором будут содержаться все выполненные ЛР
    1. Создать репозиторий в GitHub или GitLab
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git init
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git add .
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git commit -m 'Update'
    ```
    
    2. Создать структуру репозитория
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ mkdir lab_1
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ cd lab_1
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix/lab_1$ mkdir build
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix/lab_1$ mkdir doc
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix/lab_1$ mkdir src
    ```
    Далее скопируем директории folder_max и folder_min в lab_1
    
    3. Создать ветки dev / stg / prd, удалить ранее существующие ветки удаленно и локально
    Создадим фиктивную ветку fake
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git branch fake
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git branch
      fake
    * main
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git push origin fake
    ```
    Создадим ветки dev, stg, prd
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git branch dev
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git branch stg
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git branch prd
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git branch
      dev
      stg
      prd
      fake
    * main
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git push origin dev
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git push origin stg
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git push origin prd
    ```
    Удалим ветку fake локально и удаленно
    ```
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git branch -d fake
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp_and_unix$ git branch
      dev
      stg
      prd
    * main
    dimasik@DESKTOP-KTOS6NV:/usr/local/Cpp-and-Unix$ git push origin :fake
    To github.com:n0tmyself/Cpp-and-Unix.git
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
