# to run the app with docker gunicorn

    $ bash start-service

# to create linux service and start it as a linux process

    # create linux service

        sudo cat /etc/systemd/system/flask-rest-server.service >>

        [Unit]
        Description=Flask Web Application Server using Gunicorn
        After=network.target

        [Service]
        User=your_user_name
        Group=www-data
        WorkingDirectory=/home/your_user_name/flask-production
        Environment="PATH=/home/your_user_name/flask-production/venv/bin"
        ExecStart=/bin/bash -c 'source /home/your_user_name/flask-production/venv/bin/activate; gunicorn -w 3 --bind unix:/tmp/flask-rest-server/ipc.sock timez:app'
        Restart=always

        [Install]
        WantedBy=multi-user.target


    # create temp dir

        $ mkdir /tmp/flask-rest-server
    
    # enable linux service

        $ sudo systemctl enable flask-rest-server --now