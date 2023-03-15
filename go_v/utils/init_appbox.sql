
-- db:appbox--
create table app_info (id int not null primary key auto_increment,
app_name  varchar(255),
app_type varchar(255),
domain varchar(255),
stack  varchar(100),
fontport  varchar(20),
backendport  varchar(20),
delete_flg varchar(1) NOT NULL DEFAULT '0',
others  varchar(255)
) engine=InnoDB  default charset=utf8;

INSERT INTO app_info (app_name,app_type,domain,stack,fontport,backendport) values("gin-vue-admin","后台管理","gin.vue.admin.itbenyou.com","gin vue","8080","8080");
INSERT INTO app_info  (app_name,app_type,domain,stack,fontport,backendport) values("go-gin-api","代码生成","go.itbenyou.com","gin vue","8080","8080");
