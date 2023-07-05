--

CREATE TABLE clima (
    id integer NOT NULL,
    nombre character(100) NOT NULL,
    geom public.geometry(MultiPolygonZ,4326) NOT NULL
);


CREATE TABLE clima_bl (
    id integer NOT NULL,
    nombre character varying NOT NULL,
    geom public.geometry(Geometry,4326) NOT NULL
);
