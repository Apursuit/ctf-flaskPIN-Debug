# ctf-flaskPIN-Debug

## 声明

[模板原创项目地址](https://github.com/CTF-Archives/ctf-docker-template)，使用`ctf-docker-template`项目的模板

## 关于

注意：

用于测试flask pin计算的镜像，搭建一个可以允许本地用户以外用户访问`console`控制台的flask服务。测试发现默认的高版本flask已经不允许非本地用户访问console控制台了，所以这里使用了flask1.1.1以及他所需要的组件。

另外这里使用了flask1.1.1，不支持flask命令启动服务，需要在app.py里指定

启动示例：

```bash
docker run -dt -p 8080:8080 -e FLAG=flaskPIN{Cra2y4viv050} flask:PIN
```

## 环境说明

提供 `Python 3.10 + Flask` 的基础环境

## 如何使用

直接将Flask文件/项目放入 `./src` 目录即可，Flask项目主文件请使用 `app.py` 作为文件名，便于环境识别Flask项目位置

如使用了 `pycryptodome` 等第三方库，请在 `./Dockerfile` 内补充pip安装语句

源码放置进 `./src` 目录之后，执行 
```shell
docker build .
```
即可开始编译镜像

也可以在安放好相关项目文件之后，直接使用 `./docker/docker-compose.yml` 内的 `docker-compose` 文件实现一键启动测试容器

```shell
cd ./docker
docker-compose up -d
```
