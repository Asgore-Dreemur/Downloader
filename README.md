# Downloader
一个下载器,python编写,requests模块负责传输  多线程下载,不支持https,把https://改成http://即可  请在目录下创建一个config文件夹,把Download.png放进去  编译命令:pyinstaller --noconsole -F DLGUI.py --add-data=".\config\*;.\config\" -i Download.ico, 32位自行编译
