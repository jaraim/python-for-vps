import paramiko

servers = [

    {"name": "美国", "hostname": "104.194.74.122", "port": 28568, "username": "root", "password": "CThdYrDvKcuZ", "domain": "ph.jaraim.top"},   
   
    # 添加更多服务器

]

# 定义更新操作
def update_server(name, hostname, port, username, password, domain):
    try:

        # 连接服务器
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)


        print(f" {name} 更新")
        stdin, stdout, stderr = client.exec_command("apt update -y && apt install -y curl wget sudo socat")
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"更新成功")
        else:
            print(f"更新失败")
        
        print()

        print(f"{name} 安装 Docker")
        stdin, stdout, stderr = client.exec_command("curl -fsSL https://get.docker.com | sh")

        print(f"正在安装 Docker:")
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"安装 Docker 成功")
        else:
            print(f"安装 Docker 失败")

        print()

        print(f"{name} 安装 Docker Compose")
        stdin, stdout, stderr = client.exec_command('curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose')

        print(f"正在安装 Docker Compose:")
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"安装 Docker Compose 成功")
        else:
            print(f"安装 Docker Compose 失败")

        print()


        print(f"{name} 创建web目录")
        stdin, stdout, stderr = client.exec_command(" mkdir -p ./docker/web/html ./docker/web/mysql ./docker/web/certs && touch ./docker/web/nginx.conf ./docker/web/docker-compose.yml")
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"创建目录成功")
        else:
            print(f"创建目录失败")

        print()

        print(f"{name} 申请证书")
        stdin, stdout, stderr = client.exec_command("curl https://get.acme.sh | sh && ~/.acme.sh/acme.sh --register-account -m wpgabcd@outlook.com && ~/.acme.sh/acme.sh --issue -d {} --standalone".format(domain))
        print(f"正在申请中:")
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"申请成功")
        else:
            print(f"申请失败")

        print()

        print(f"{name} 下载证书")
        stdin, stdout, stderr = client.exec_command("~/.acme.sh/acme.sh --installcert -d {} --key-file ./docker/web/certs/key.pem --fullchain-file ./docker/web/certs/cert.pem".format(domain))
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"下载证书成功")
        else:
            print(f"下载证书失败")

        print()        

        print(f"{name} 配置nginx")
        stdin, stdout, stderr = client.exec_command('wget -O ./docker/web/nginx.conf https://raw.githubusercontent.com/jaraim/My-project/main/docker/nginx/nginx.conf && sed -i "s/ph.jaraim.top/' + domain + '/g" ./docker/web/nginx.conf')
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"配置成功")
        else:
            print(f"配置失败")

        print()

        print(f"{name} 配置docker-compose.yml")
        stdin, stdout, stderr = client.exec_command('wget -O ./docker/web/docker-compose.yml https://raw.githubusercontent.com/jaraim/My-project/main/docker/cms/compose.yml')
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"配置成功")
        else:
            print(f"配置失败")

        print()

        print(f"{name} 下载网站源码-苹果CMS")
        stdin, stdout, stderr = client.exec_command('cd /home/web && wget https://github.com/magicblack/maccms_down/raw/master/maccms10.zip && sudo apt-get install -y unzip && unzip maccms10.zip -d html && rm maccms10.zip && mv /home/web/html/maccms10-master /root/docker/web/html/')
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"下载成功")
        else:
            print(f"下载失败")

        print()

        print(f"{name} 下载电影先生2.0模板")
        stdin, stdout, stderr = client.exec_command('./docker/web/html/template/ && wget https://github.com/kejilion/Website_source_code/raw/main/DYXS2.zip && unzip DYXS2.zip && rm ./docker/web/html/template/DYXS2.zip && ./docker/web/html/template/DYXS2/asset/admin/Dyxs2.php ./docker/web/html/application/admin/controller && ./docker/web/html/template/DYXS2/asset/admin/dycms.html ./docker/web/html/application/admin/view/system')
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"下载成功")
        else:
            print(f"下载失败")

        print()

        print(f"{name} 修改后台入口文件名为vip.php")
        stdin, stdout, stderr = client.exec_command('mv /root/docker/web/html/admin.php /root/docker/web/html/vip.php && wget -O /root/docker/web/html/application/extra/maccms.php https://raw.githubusercontent.com/kejilion/Website_source_code/main/maccms.php')
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"设置成功")
        else:
            print(f"设置失败")

        print()

        print(f"{name} 启动环境")
        stdin, stdout, stderr = client.exec_command('cd docker/web && docker-compose up -d')
        print(f"启动中:")
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"启动成功")
        else:
            print(f"启动失败")

        print()


        print(f"{name} 赋予文件权限")
        stdin, stdout, stderr = client.exec_command('docker exec nginx chmod -R 777 /var/www/html && docker exec php chmod -R 777 /var/www/html')
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"赋予成功")
        else:
            print(f"赋予失败")

        print()

        print(f"{name} 安装PHP依赖")
        stdin, stdout, stderr = client.exec_command('docker exec php apt update && docker exec php apt install -y libmariadb-dev-compat libmariadb-dev libzip-dev && docker exec php docker-php-ext-install pdo_mysql zip && docker restart php')
        print(f"安装中:")
        while not stdout.channel.exit_status_ready():
            if stdout.channel.recv_ready():
                print(stdout.channel.recv(1024).decode(), end="")

        # 检查执行状态
        if stderr.channel.recv_exit_status() == 0:
            print(f"安装成功")
        else:
            print(f"安装失败")

        print()

        print(f"搭建完成\nhttps://{domain}")
        print()
        print()

        # 关闭 SSH 连接
        client.close()


    except Exception as e:
        print(f"连接 {name} 失败")


# 遍历服务器列表，逐一更新
for server in servers:
    name = server["name"]
    hostname = server["hostname"]
    port = server["port"]
    username = server["username"]
    password = server["password"]
    domain = server["domain"]
    update_server(name, hostname, port, username, password, domain)

# 等待用户按下任意键后关闭窗口
input("按任意键关闭窗口...")


