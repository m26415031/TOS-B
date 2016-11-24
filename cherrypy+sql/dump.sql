PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE tbl1(one varchar(10), two smallint);
INSERT INTO "tbl1" VALUES('hello!',10);
INSERT INTO "tbl1" VALUES('goodbye',20);
COMMIT;
