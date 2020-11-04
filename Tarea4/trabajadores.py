class Trabajador:
    def __init__(self, num, nombre, paterno, materno, horas, sueldo, anio):
        self.__num_trabajador = num
        self.__nombre = nombre
        self.__paterno = paterno
        self.__materno = materno
        self.__horas_extras = horas
        self.__sueldo_base = sueldo
        self.__anio_ingreso = anio

    def set_num_trabajador(self, num):
        self.__num_trabajador = num

    def get_num_trabajador(self):
        return self.__num_trabajador

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_paterno(self, paterno):
        self.__paterno = paterno

    def get_paterno(self):
        return self.__paterno

    def set_materno(self, materno):
        self.__materno = materno

    def get_materno(self):
        return self.__materno

    def set_horas_extras(self, horas):
        self.__horas_extras = horas

    def get_horas_extras(self):
        return self.__horas_extras

    def set_sueldo_base(self, sueldo):
        self.__sueldo_base = sueldo

    def get_sueldo_base(self):
        return self.__sueldo_base

    def set_anio_ingreso(self, anio):
        self.__anio_ingreso = anio

    def get_anio_ingreso(self):
        return self.__anio_ingreso

    def sueldos(self, trabajador):
        if (int(trabajador.__anio_ingreso)) < 2020:
            prestaciones = (2020 - (int(trabajador.__anio_ingreso)))
            sueldo = (int(trabajador.__horas_extras)*276.5) + (int(trabajador.__sueldo_base)) + (prestaciones*3)
            print("")
            print(f"El trabajador {trabajador.__nombre} {trabajador.__paterno} {trabajador.__materno} tiene un salario de {sueldo} mas prestaciones del {prestaciones*3}% ")

        else:
            sueldo = (int(trabajador.__horas_extras)*276.5) + (int(trabajador.__sueldo_base))
            print("")
            print(f"El trabajador {trabajador.__nombre} {trabajador.__paterno} {trabajador.__materno} tiene un salario de {sueldo} y prestaciones del 0%")


