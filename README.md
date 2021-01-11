# Python_ORC

下载该文件夹，检查系统是否装有docker 和 docker compose，
如果没有docker和docker compose，可以直接下载桌面版，里面内置了docker 和 docker compose。  
Mac: https://hub.docker.com/editions/community/docker-ce-desktop-mac/  
Windows: https://hub.docker.com/editions/community/docker-ce-desktop-windows/  
确保docker启动后  
确保电脑里又Postman


在该文件夹下执行以下命令 

docker-compose build

docker-compose up


在Postman里输入 http://0.0.0.0:8000/index
request type选择POST， 然后用body上传， key输入movie_image,  value则上传本地任意图片，最后点击Send

结果会已json格式返回所有的字母。

