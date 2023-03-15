package main

import (
	"appbox/routers"
)

func main() {
	// 创建数据库
	// sql: CREATE DATABASE bubble;

	// // 连接数据库
	// err := utils.InitMySQL()
	// if err != nil {
	// 	panic(err)
	// }

	// defer utils.Close() // 程序退出关闭数据库连接
	// // 模型绑定
	// utils.DB.AutoMigrate(&models.Todo{})

	// 注册路由

	r := routers.SetupRouter()
	r.Run()
}
