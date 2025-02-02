DROP TABLE IF EXISTS stage.admin_taxes CASCADE;

DROP TABLE IF EXISTS stage.admin_codes CASCADE;
DROP TABLE IF EXISTS stage.admin_apartment CASCADE;
DROP TABLE IF EXISTS stage.admin_building CASCADE;
DROP TABLE IF EXISTS stage.admin_entry CASCADE;

DROP TABLE IF EXISTS stage.immoscout_kaufen CASCADE;
DROP TABLE IF EXISTS stage.immoscout_mieten CASCADE;
DROP TABLE IF EXISTS stage.immoscout_keywords;

DROP SCHEMA IF EXISTS stage;


DROP TABLE IF EXISTS public.admin_taxes CASCADE;
DROP TABLE IF EXISTS public.admin_entry CASCADE;
DROP TABLE IF EXISTS public.admin_apartment CASCADE;
DROP TABLE IF EXISTS public.admin_building CASCADE;
DROP TABLE IF EXISTS public.admin_codes CASCADE;
DROP TABLE IF EXISTS public.admin_stockwerk;
DROP TABLE IF EXISTS public.admin_buildingklasse;
DROP TABLE IF EXISTS public.admin_heizung1;
DROP TABLE IF EXISTS public.admin_heizung2;
DROP TABLE IF EXISTS public.admin_Wasser1;
DROP TABLE IF EXISTS public.admin_Wasser2;
DROP TABLE IF EXISTS public.admin_BuildingStatus;
DROP TABLE IF EXISTS public.admin_strassen_sprache;
DROP TABLE IF EXISTS public.admin_apartment_status;

DROP TABLE IF EXISTS public.immoscout_mieten CASCADE;
DROP TABLE IF EXISTS public.immoscout_kaufen CASCADE;
DROP TABLE IF EXISTS public.immoscout_keywords;


