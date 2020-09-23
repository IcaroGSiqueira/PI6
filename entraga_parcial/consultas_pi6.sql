select Ocupação.CPU_Uso, Ocupação.GPU_Uso, Ocupação.GPU_MB, Ocupação.RAM_Usada, Ocupação.RAM_Livre, 
Performance.CPU_Mhz, Performance.GPU_Mhz, Performance.Rede_Kbps, 
Temperaturas.CPU_ºC, Temperaturas.GPU_ºC, Temperaturas.HDD_ºC, Temperaturas.SSD_ºC, Temperaturas.Data_Hora
from Ocupação 
inner join  Performance on Performance.Data_Hora = Ocupação.Data_Hora 
inner join Temperaturas on Temperaturas.Data_Hora = Performance.Data_Hora;

select Ocupação.CPU_Uso, Performance.CPU_Mhz, Temperaturas.CPU_ºC, Temperaturas.Data_Hora from Ocupação 
inner join  Performance on Performance.Data_Hora = Ocupação.Data_Hora 
inner join Temperaturas on Temperaturas.Data_Hora = Performance.Data_Hora group by Data_Hora order by Data_Hora;

select Ocupação.GPU_Uso, Ocupação.GPU_MB, Performance.GPU_Mhz, Temperaturas.GPU_ºC, Temperaturas.Data_Hora from Ocupação 
inner join  Performance on Performance.Data_Hora = Ocupação.Data_Hora 
inner join Temperaturas on Temperaturas.Data_Hora = Performance.Data_Hora group by Data_Hora order by Data_Hora;

select * from Temperaturas order by Data_Hora;

select * from Ocupação order by Data_Hora;

select * from Performance order by Data_Hora;

-- ----------------------------------------- Consultas ao Banco de Dados ------------------------------------------------

select Ocupação.CPU_Uso, Performance.CPU_Mhz, Temperaturas.CPU_ºC, Temperaturas.Data_Hora from Ocupação 
inner join  Performance on Performance.Data_Hora = Ocupação.Data_Hora 
inner join Temperaturas on Temperaturas.Data_Hora = Performance.Data_Hora group by Data_Hora order by CPU_Mhz desc;

select Ocupação.CPU_Uso, Ocupação.GPU_Uso, Ocupação.RAM_Usada, Ocupação.RAM_Livre, 
Performance.CPU_Mhz, Performance.GPU_Mhz, 
Temperaturas.CPU_ºC, Temperaturas.SSD_ºC, Temperaturas.Data_Hora
from Ocupação 
inner join  Performance on Performance.Data_Hora = Ocupação.Data_Hora 
inner join Temperaturas on Temperaturas.Data_Hora = Performance.Data_Hora group by Data_Hora order by RAM_Usada desc;

select Ocupação.CPU_Uso, Ocupação.RAM_Usada, Ocupação.RAM_Livre, Performance.CPU_Mhz, 
Temperaturas.CPU_ºC, Temperaturas.GPU_ºC, Temperaturas.HDD_ºC, Temperaturas.SSD_ºC, Temperaturas.Data_Hora
from Ocupação 
inner join  Performance on Performance.Data_Hora = Ocupação.Data_Hora 
inner join Temperaturas on Temperaturas.Data_Hora = Performance.Data_Hora group by Data_Hora order by CPU_ºC desc;

select Ocupação.GPU_Uso, Ocupação.GPU_MB, Performance.GPU_Mhz, 
Temperaturas.GPU_ºC, Temperaturas.Data_Hora
from Ocupação 
inner join  Performance on Performance.Data_Hora = Ocupação.Data_Hora 
inner join Temperaturas on Temperaturas.Data_Hora = Performance.Data_Hora group by Data_Hora order by GPU_Mhz desc;
