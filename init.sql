
create database Data;

use Data;

-- grant select, insert, update, delete on Data.* to 'da'@'localhost' identified by 'da';

create table NormalHour (
    `id` smallint not null auto_increment,
    `month` varchar(50) not null,
    `year` smallint not null,
    `TargetHour` smallint not null,
    primary key (`id`)
) engine=innodb default charset=utf8;

insert into NormalHour (month, year, targethour) values ("Jan", 2017, 144);
insert into NormalHour (month, year, targethour) values ("Feb", 2017, 152);
insert into NormalHour (month, year, targethour) values ("Mar", 2017, 184);
insert into NormalHour (month, year, targethour) values ("Apr", 2017, 144);
insert into NormalHour (month, year, targethour) values ("May", 2017, 168);
insert into NormalHour (month, year, targethour) values ("Jun", 2017, 176);
insert into NormalHour (month, year, targethour) values ("Jul", 2017, );
insert into NormalHour (month, year, targethour) values ("Aug", 2017, );
insert into NormalHour (month, year, targethour) values ("Sep", 2017, );
insert into NormalHour (month, year, targethour) values ("Oct", 2017, );
insert into NormalHour (month, year, targethour) values ("Nov", 2017, );
insert into NormalHour (month, year, targethour) values ("Dec", 2017, );
