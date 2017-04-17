drop table if exists user;
create table user (
  id integer PRIMARY key auto_increment,
  username text not NULL,
  email text not NULL,
  authenticated boolean not NULL
);