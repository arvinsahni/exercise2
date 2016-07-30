CREATE FUNCTION up_in(wordin TEXT) RETURNS VOID AS
$$
BEGIN
     	LOOP
            	UPDATE tweetwordcount SET count = count +1  WHERE word = wordin;
                IF found THEN
                        RETURN;
                END IF;
                BEGIN
                     	INSERT INTO tweetwordcount (word,count) VALUES (wordin, 1);
                        RETURN;
                EXCEPTION WHEN unique_violation THEN
                END;
        END LOOP;
END;
$$ LANGUAGE plpgsql;
