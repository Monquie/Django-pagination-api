#!/bin/bash

image=mysql:8.0.30
program=${0}
defaultdb=tingpay
container=tingpaydb
expose_port=3307
network=vidivadev

function usage {
    echo "usage: $program [-udh] <database_name>";
    echo "  -u <database_name>     up database";
    echo "  -d                     down database";
    echo "  -l                     view database logs";
    echo "  -h                     display help";
    exit 1;
}

main() {
    # no argument
    # print usage and exit
    [ $# -eq 0 ] && { 
        usage; 
        exit 1; 
    }
    task=${1};
    db=${2};
    case $task in 
        "-u")
            if [ "$db" == "" ]; then db=$defaultdb; fi
            db_name=$db"_db"
            echo "running database $db_name...";
            stop_db
            start_db $db_name
            ;;

        "-d")
            echo "stoping tingpay_db...";
            stop_db
            ;;

        "-l")
            echo "showing tingpay_db logs...";
            show_db_logs
            ;;

        "-h")
            usage; 
            exit 1; 
            ;;

        *)
            exit 1; 
            ;;
    esac
}

start_db(){
    environment="-e MYSQL_ROOT_PASSWORD=divawallet  -e MYSQL_ROOT_HOST=\"%\""
    volumes="-v $(pwd)/database/db_data/$db_name/:/var/lib/mysql/ -v $(pwd)/database/dbconf/:/etc/mysql/ -v $(pwd)/database/dbinit:/docker-entrypoint-initdb.d/"
    docker_command="mysqld --default-authentication-plugin=mysql_native_password"
    cmd="docker run -d --name $container -p $expose_port:3306 --network $network $environment $volumes $image $docker_command"
    echo $cmd
    eval $cmd 
}

stop_db(){
    id=`docker ps | grep :$expose_port | cut -d' ' -f1`
    if [ -n "$id" ]; then
        cmd="docker stop $id"
        echo $cmd
        eval $cmd
    fi
    remove_docker_container
}

show_db_logs(){
    id=`docker ps | grep :$expose_port | cut -d' ' -f1`
    if [ -n "$id" ]; then
        cmd="docker logs -f $id"
        echo $cmd
        eval $cmd
    fi
}

remove_docker_container(){
    id=`docker ps -a| grep $container | cut -d' ' -f1`
    if [ -n "$id" ]; then
        cmd="docker container rm $id"
        echo $cmd
        eval $cmd
    fi
}

main $@