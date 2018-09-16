### 已实现的功能
#### 资产数据收集接口
在`/assets/report`下提供一个接受post请求的开放接口
能接收任意来源的数据。

#### 仪表盘页面
从数据库调出已有资产的设备状态和数量统计，发送给前端页面展示：
![dashboard](http://imglf4.nosdn0.126.net/img/c09lVS9TR3YrUFlzK3dhNFJtSHc3R3BhdVpjN3dETWpTSURBMWRNNFdWUmc0ekkxZVNZUlF3PT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

#### 资产列表
![datatables](http://imglf6.nosdn0.126.net/img/c09lVS9TR3YrUFlzK3dhNFJtSHc3TjNrU0FOT0E1YXZXVWNhU3RNMlI4V3FZT0lTWUU3QVFnPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

#### 资产详情
![detail](http://imglf6.nosdn0.126.net/img/c09lVS9TR3YrUFlzK3dhNFJtSHc3RDJTbVIvUERWT09nVUxxd09KL1JHZVFJWXFiR3M4TW93PT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

### 待完善
#### 客户端
目前服务端展示的数据都是通过测试脚本发送的虚拟数据，仍需要解决客户端自动收集自身设备信息并自动发送给服务端的功能。

#### 服务端

仍需实现平台的登陆验证功能，以保证信息的安全性。

![login_require](http://imglf3.nosdn0.126.net/img/c09lVS9TR3YrUFlzK3dhNFJtSHc3QWV0dFowQm5QTTJOZ1ZWTzNTVG04QUR4VEQ1ZnRLalZRPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)
