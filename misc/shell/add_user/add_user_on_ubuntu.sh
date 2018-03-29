#!/usr/bin/env bash
for username in zengyuetian zhangshuwei donghao zengwenye sunxiaolei zhoujingya wangkang jinyifan renyongning
    do
        useradd -g admin $username;
        mkdir /home/$username;
        chown $username  /home/$username;
        chgrp admin /home/$username;
        cp .bashrc /home/$username/;
        chown  $username. /home/$username/.bashrc;
        cp .profile /home/$username/;
        chown  $username. /home/$username/.profile;
        chsh -s /bin/bash $username;
        passwd $username;
    done
