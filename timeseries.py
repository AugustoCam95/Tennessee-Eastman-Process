#IMPORTAÇÃO DE MÓDULOS
import os
#import pandas as pd
#import math
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

labely = ['A FEED (unit = kscmh)','D FEED (unit = kg/hr)','E FEED (unit = kg/hr)','Total FEED (unit = kscmh)','Recycle Flow (unit = kscmh)','Reactor Feed Rate (unit = kscmh)','Reactor Pressure (unit = kPa gauge)',
'Reactor Level (unit = %)','Reactor Temperature (unit = Deg C)','Purge Rate(Stream 9) (unit = kscmh)','Product Sep Temp (unit = Deg C)','Product Sep Level (unit = %)','Prod Sep Pressure (unit = kPa gauge)',
'Prod Sep Underflow (unit = m³/hr)','Stripper Level (unit = %)','Stripper Pressure (unit = kPa gauge)','Stripper Underflow (unit = m³/hr)','Stripper Temperature (unit = Deg C)','Stripper Steam FLow (unit = kg/hr)',
'Compressor Work (unit = kW)','Reactor Cooling Water Outlet Temp (unit = Deg C)','Separator Cooling Water Outlet Temp (unit = Deg C)','% mole of Component A' ,'% mole of Component B' ,'% mole of Component C', 
'% mole of Component D','% mole of Component E','% mole of Component F','% mole of Component A','% mole of Component B','% mole of Component C','% mole of Component D','% mole of Component E','% mole of Component F',
'% mole of Component G','% mole of Component H','% mole of Component D','% mole of Component E','% mole of Component F','% mole of Component G','% mole of Component H','D Feed Flow',
'E Feed Flow','A Feed Flow','Total Feed Flow','Compressor Recycle Valve','Purge Valve','Separator Pot Liquid Flow','Stripper Liquid Product Flow','Stripper Steam Valve',
'Reactor Cooling Water Flow','Condenser Cooling Water Flow','Agitator Speed']                                                     

#Make directors
for t in range(22):
	newpath = r'/home/jose/Documentos/data/data{}'.format(t)
	newpathte = r'/home/jose/Documentos/data/data{}_te'.format(t)
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	if not os.path.exists(newpathte):
		os.makedirs(newpathte)

for t in range(22):
	newpath = r'/home/jose/Documentos/data/correlation{}'.format(t)
	newpathte = r'/home/jose/Documentos/data/correlation{}_te'.format(t)
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	if not os.path.exists(newpathte):
		os.makedirs(newpathte)



#principal loop
for i in range(22):
	
	print("LAÇO: {}".format(i))

	#access files
	if(i<10):
		archive =  np.loadtxt('d0{}.dat'.format(i))
		archivete = np.loadtxt('d0{}_te.dat'.format(i))		
	else:
		archive =  np.loadtxt('d{}.dat'.format(i))
		archivete = np.loadtxt('d{}_te.dat'.format(i))

	#verificação de linha e coluna archive dat
	if( i == 0):
		archive = archive.transpose()
	if( archive.shape[1] > archive.shape[0]):
	 	archive = archive.transpose()
	
	#verificação de linha e coluna archive DAT_TE
	if( i== 0):
		archivete = archivete.transpose()
	if( archivete.shape[1] > archivete.shape[0]):
		archivete = archivete.transpose()

	#shape dat
	print('Shape dat')
	print(archive.shape)
	menor = archive.shape[1]
	maior = archive.shape[0]

	#shape datTE
	print('Shape DAT_TE')
	print(archivete.shape)
	menor_te = archivete.shape[1]
	maior_te = archivete.shape[0]

	#montando matriz com médias
	avg = np.zeros( menor )
	avg_te = np.zeros( menor_te )

	for j in range( menor ):
		avg[j] = np.median(archive[:,j])

	
	for j in range( menor_te ):
		avg_te[j] = np.median(archivete[:,j])
	
	matrix_avg = np.zeros( (maior , menor) )
	matrix_avg_te = np.zeros(( maior_te, menor_te))

	for k in range( maior ):
		for l in range( menor ):
			matrix_avg[k,l] = avg[l]

	for w in range( maior_te):
		for q in range( menor_te):
			matrix_avg_te[w,q] = avg_te[q]
	#print('Matriz de medias:\n')
	#print(matrix_avg)
 
	#montando matriz com desvio padrao

	std = np.zeros( menor )
	std_te = np.zeros( menor_te)


	for j in range( menor ):
		std[j] = np.std(archive[:,j])

	for j in range( menor_te):
		std_te[j] = np.std(archivete[:,j])


	#print('Desvio:\n')
	#print(std)

	matrix_std = np.zeros((maior, menor))
	matrix_std_te = np.zeros((maior_te, menor_te))

	for k in range(maior):
		for l in range(menor):
			matrix_std[k,l] = std[l]

	for k in range(maior_te):
		for l in range(menor_te):
			matrix_std_te[k,l] = std_te[l]

	#print('Matriz de desvios:\n')
	#print(matrix_std)

	#montado desvios para o gráfico
	desvio_positivo = matrix_std + matrix_avg
	desvio_negativo = matrix_avg - matrix_std
	desvio_positivo_te = matrix_std_te + matrix_avg_te
	desvio_negativo_te = matrix_avg_te - matrix_std_te


	#montando média data0 
	d00 = np.loadtxt('d00.dat')
	data0 = d00.transpose()
	

	avg_data0 = np.zeros( data0.shape[1] )

	for j in range(data0.shape[1]):
		avg_data0[j] = np.median(data0[:,j])

		
	matrix_avg_data0 = np.zeros(( data0.shape[0], data0.shape[1]))
	
	for k in range(data0.shape[0]):
		for l in range(data0.shape[1]):
			matrix_avg_data0[k,l] = avg_data0[l]

	#montando média data0_te
	d00te = np.loadtxt('d00_te.dat')

	if( d00te.shape[1] > d00te.shape[0]):
		d00te = d00te.transpose()

	avg_data0_te = np.zeros( d00te.shape[1] )

	for j in range(d00te.shape[1]):
		avg_data0_te[j] = np.median(d00te[:,j])

	matrix_avg_data0_te = np.zeros(( d00te.shape[0], data0.shape[1]))

	for k in range(d00te.shape[0]):
		for l in range(d00te.shape[1]):
			matrix_avg_data0_te[k,l] = avg_data0_te[l]




	#gerando gráficos e montando figuras
	for j in range(52):
		fig, ax = plt.subplots(figsize = (15,5))
		if(j < 41):
			plt.title('Variavel XMEAS-{} FAULT:{}'.format(j,i))
		else:
			plt.title('Variavel XMV-{} FAULT:{}'.format(j,i))
		plt.plot(archive[:,j], color = 'black')
		plt.plot(desvio_positivo[:,j],'g--' ,label = '+std')
		plt.legend(loc = 'lower right')
		
		if( j > 0 ):	
			plt.plot(matrix_avg_data0[:,j], color = 'blue', label = 'avg_data0')
			plt.legend(loc = 'lower right' )
		
		plt.plot(desvio_negativo[:,j],'g--' ,label = '-std')
		plt.legend(loc = 'lower right')
		plt.plot(matrix_avg[:,j], 'r',label = 'avg')
		plt.legend(loc = 'lower right')
		
		#subtitle for each graphic
		if( j <  21):
			plt.ylabel(labely[j])
			plt.xlabel('Process measurements (3 minute sampling interval)')
		if(( 20 < j ) and ( j < 35 ) ):
			plt.ylabel(labely[j])
			plt.xlabel('Process measurements (6 minute sampling interval)')
		if(( 35 < j ) and ( j < 41 ) ):
			plt.ylabel(labely[j])
			plt.xlabel('Process measurements (15 minute sampling interval)')
		if(( 40 < j ) and ( j < 53 ) ):
			plt.ylabel(labely[j])
			plt.xlabel('Process measurements (3 minute sampling interval)')

		#save plots
		if(j < 41):
			plt.savefig('data{}/XMEAS-{}-FAULT:{}.pdf'.format(i,j,i))
		else:
			plt.savefig('data{}/XMV-{}-FAULT:{}.pdf'.format(i,j,i))
		plt.close(fig)



	#make graphics and edit
	for j in range(52):
		fig, ax = plt.subplots(figsize = (15,5))
		if(j < 41):
			plt.title('Variavel XMEAS-{} FAULT:{}'.format(j,i))
		else:
			plt.title('Variavel XMV-{} FAULT:{}'.format(j,i))
		plt.plot(archivete[:,j], color = 'black')
		plt.plot(desvio_positivo_te[:,j],'g--' ,label = '+std')
		plt.legend(loc = 'lower right')
		
		if( j > 0 ):	
			plt.plot(matrix_avg_data0[:,j], color = 'blue', label = 'avg_data0')
			plt.legend(loc = 'lower right' )

		plt.plot(desvio_negativo_te[:,j],'g--' ,label = '-std')
		plt.legend(loc = 'lower right')
		plt.plot(matrix_avg_te[:,j], 'r',label = 'avg')
		plt.legend(loc = 'lower right')

		#subtitle for each graphic
		if( j <  21):
			plt.ylabel(labely[j])
			plt.xlabel('Process measurements (3 minute sampling interval)')
		if(( 20 < j ) and ( j < 35 ) ):
			plt.ylabel(labely[j])
			plt.xlabel('Process measurements (6 minute sampling interval)')
		if(( 35 < j ) and ( j < 41 ) ):
			plt.ylabel(labely[j])
			plt.xlabel('Process measurements (15 minute sampling interval)')
		if(( 40 < j ) and ( j < 53) ):
			plt.ylabel(labely[j])
			plt.xlabel('Process measurements (3 minute sampling interval)')
	

		#save plots
		if(j < 41):
			plt.savefig('data{}_te/XMEAS-{}-FAULT:{}.pdf'.format(i,j,i))
		else:
			plt.savefig('data{}_te/XMV-{}-FAULT:{}.pdf'.format(i,j,i))
		plt.close(fig)


	#correlation
	for j in range(52):
		fig, ax = plt.subplots(figsize = (15,5))
		if(j < 51):
			plt.scatter(archive[:,j],archive[:,j+1])
			if(j < 41):
				plt.savefig('correlation{}/XMEAS-({},{})-FAULT:{}.pdf'.format(i,j,j+1,i))
			else:
				plt.savefig('correlation{}/XMV-({},{})-FAULT:{}.pdf'.format(i,j,j+1,i))
		plt.close(fig)


	for j in range(52):
		fig, ax = plt.subplots(figsize = (15,5))
		if(j < 51):
			plt.scatter(archivete[:,j],archivete[:,j+1])
			if(j < 41):
				plt.savefig('correlation{}_te/XMEAS-({},{})-FAULT:{}.pdf'.format(i,j,j+1,i))
			else:
				plt.savefig('correlation{}_te/XMV-({},{})-FAULT:{}.pdf'.format(i,j,j+1,i))
		plt.close(fig)





