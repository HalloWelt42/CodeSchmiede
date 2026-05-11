SELECT name, alter_jahre, CASE   WHEN alter_jahre < 30 THEN 'jung'   WHEN alter_jahre < 50 THEN 'mittel'   ELSE 'reif' END AS gruppe FROM leser ORDER BY alter_jahre;
