drop table if exists user;
create table user (
  id integer PRIMARY key autoincrement,
  username text not NULL,
  email text not NULL,
  authenticated text not NULL
);