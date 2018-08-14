# Thrift RPC service

Install Apache Thrift

```
brew unlink thrift
brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/9d524e4850651cfedd64bc0740f1379b533f607d/Formula/thrift.rb
```

Firstly, finish thrift file, then run

```
thrift -r -gen py task.thrift
```
Then finish client and server

![dir](https://ws3.sinaimg.cn/large/0069RVTdly1fu972gae6mj30fm0n6765.jpg)

Intro of Thrift
[https://en.wikipedia.org/wiki/Apache_Thrift](https://en.wikipedia.org/wiki/Apache_Thrift)

Intro of RPC
[https://en.wikipedia.org/wiki/Remote_procedure_call](https://en.wikipedia.org/wiki/Remote_procedure_call)