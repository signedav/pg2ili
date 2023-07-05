--

CREATE TABLE clima (
    id integer NOT NULL,
    nombre character(100) NOT NULL,
    geom geometry(MultiPolygonZ,4326) NOT NULL
);

CREATE TABLE clima_bl (
    id integer NOT NULL,
    nombre character varying NOT NULL,
    geom geometry(Geometry,4326) NOT NULL
);
