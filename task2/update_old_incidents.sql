CREATE OR REPLACE PROCEDURE update_old_incidents()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE incidents
    SET status = 'in_progress'
    WHERE status = 'new'
      AND created_at < NOW() - INTERVAL '3 days';
END;
$$;

CALL update_old_incidents();

SELECT * FROM incidents
WHERE status = 'in_progress'
ORDER BY created_at;
