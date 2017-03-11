# 介绍

Kont BS 是一个博客管理系统，使用 Django 1.9 构建，支持 Python 2.7+ 以上启动。

支持 Django ORM 所支持的数据库，推荐使用 MySQL 5.5+ 以上的版本。

点击查看我的 [个人网站](https://hexiangyu.me)，使用 Athena 构建。

如果你擅长使用 Python 和 拥有 Python Web 开发能力，欢迎 [贡献代码](/about/contributing.md) 和我一起完善 Kont BS。

## 主要功能

1. Markdown 格式的文章发布
2. 文章的管理，包括增删改查功能
3. 统计每篇文章阅读量
4. 个人简历功能（响应式）

## 版本信息

Athena 采用的版本号采用语义化版本，格式为 `主版本号.次版本号.修订号`。

- 主版本号：大量新功能上线，或者发布不兼容版本
- 次版本号：上线小功能，不影响其他功能
- 修订号：修复 BUG 

## TODO

版本 | 功能 | 预计上线时间
:----------- | :----------- | :-----------
0.2.0         | 剥离全部硬编码，放入数据库作为可配置功能 | 暂无