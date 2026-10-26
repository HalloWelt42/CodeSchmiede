SELECT name, kolonie, lieblingsfisch
FROM pinguine
WHERE kolonie IN ('Süd', 'Ost') AND lieblingsfisch IN ('Hering', 'Lachs');
