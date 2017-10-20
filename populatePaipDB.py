import psycopg2 as pg2
import psycopg2.extras as pg2ex
import sys

con = pg2.connect(host='localhost', user='openerp', password='postgres',dbname='paip_db')
c = con.cursor(cursor_factory = pg2ex.DictCursor)

zero = 0
t = True
f = False

disciplinas = [('QXD0108','Introdução à Ciência da Computação',64),
	('QXD0001','Fundamentos de Programação',96),
	('QXD0005','Arquitetura de Computadores',64),
	('QXD0056','Matemática Básica',64),
	('QXD0103','Ética, Direito e Legislação',32),
	('QXD0109','Pré-Cálculo',32),
	
	('QXD0007','Programação Orientada a Objetos',64),
	('QXD0013','Sistemas Operacionais',64),
	('QXD0010','Estrutura de Dados',64),
	('QXD0006','Cálculo Diferencial e Integral I ',64),
	('QXD0008','Matemática Discreta',32),
	
	('QXD0114','Programação Funcional',64),
	('QXD0115','Estrutura de Dados Avançada',64),
	('QXD0040','Linguagens Formais e Autômatos',64),
	('QXD0017','Lógica para Computação',64),
	('QXD0012','Probabilidade e Estatística',64),
	
	('QXD0011','Fundamentos de Banco de Dados ',64),
	('QXD0016','Linguagens de Programação ',64),
	('QXD0041','Projeto e Análise de Algoritmos',64),
	('QXD0116','Álgebra Linear ',64),
	('QXD0014','Análise e Projeto de Sistemas',64),
	
	('QXD0025','Compiladores ',64),
	('QXD0119','Computação Gráfica ',64),
	('QXD0120','Matemática Computacional',64),
	('QXD0021','Redes de Computadores ',64),
	('QXD0020','Desenvolvimento de Software para Web',64),
	
	('QXD0019','Engenharia de Software ',64),
	('QXD0038','Interface Humano-Computador ',64),
	('QXD0043','Sistemas Distribuídos',64),
	('QXD0037','Inteligência Artificial ',64),
	('QXD0046','Teoria da Computação',32),
	
	('QXD0110','Projeto de Pesquisa Científica e Tecnológica ',32),
	('QXD0157','Trabalho de Conclusão de Curso I ',32),
	('QXD0155','Estágio Supervisionado I',160),
	('QXD0029','Empreendedorismo ',64),
	
	('QXD0158','Trabalho de Conclusão de Curso II ',96),
	('QXD0156','Estágio Supervisionado II ',160),

	('QXD0187','Tópicos Especiais I',64),
	('QXD0175','Tópicos Especiais II	',64),
	('QXD0174','Tópicos Especiais III',64),
	('QXD0173','Tópicos Especiais IV',64),
	('QXD0035','Inglês Instrumental I',64),
	('QXD0036','Inglês Instrumental II',64),
	('QXD0058','Projeto Detalhado de Software',64),
	('QXD0061','Requisitos de Software',64),
	('QXD0060','Processos de Software',64),
	('QXD0068','Reuso de Software',64),
	('QXD0042','Qualidade de Software',64),
	('QXD0023','Gerência de Projetos de Software',64),
	('QXD0063','Verificação e Validação',64),
	('QXD0062','Manutenção de Software	',64),
	('QXD0069','Segurança',64),
	('QXD0073','Experimentação em Engenharia de Software	',64),
	('QXD0075','Redes Sociais	',64),
	('QXD0090','Redes de Comunicações Móveis	',64),
	('QXD0048','Tópicos Avançados em Redes de Computadores	',64),
	('QXD0113','Língua Brasileira de Sinais	',64),
	('QXD0169','Modelagem e Simulação Discreta de Sistemas	',64),
	('QXD0185','Análise de Desempenho de Sistemas	',64),
	('QXD0167','Teoria da Prova	',64),
	('QXD0172','Lógica Modal	',64),
	('QXD0152','Teoria dos Grafos	',64),
	('QXD0181','Pesquisa Operacional	',64),
	('QXD0171','Otimização Combinatória	',64),
	('QXD0168','Algoritmos Probabilísticos	',64),
	('QXD0186','Cálculo Numérico	',64),
	('QXD0183','Computação Paralela	',64),
	('QXD0177','Recuperação de Informação	',64),
	('QXD0076','Sistemas Multiagentes	',64),
	('QXD176','Aprendizado de Máquina	',64),
	('QXD0178','Mineração de Dados	',64),
	('QXD0179','Estatística Multivariada	',64),
	('QXD018','Construção de Sistemas de Gerência de Banco de Dados	',64),
	('QXD0170','Criptografia',64),
	('QXD0188','Processamento de Imagens	',64),
	('QXD0182','Visão Computacional	',64),	
	('QXD0184','Realidade Virtual	',64),
	('QXD0044','Sistemas Multimídia	',64),
	('QXD0078','Introdução ao Desenvolvimento de Jogos	',64),
	('QXD0134','Cálculo Diferencial e Integral II	',64),
	('QXD0180','Física I',64),
	('QXD0099','Desenvolvimento de Software para Persistência	',64),
	('QXD0153','Desafios de Programação	',64),
	('PRG0002','Relações Étnico-Raciais e Africanidades	',64),
	('PRG0003','Educação Ambiental	',64),
	('PRG0004','Educação em Direitos Humanos	',64),
	]

preRequisitos = [('QXD0108',['']),
				('QXD0001',['']),
				('QXD0005',['']),
				('QXD0056',['']),
				('QXD0103',['']),
				('QXD0109',['']),
				
				('QXD0007',['QXD0001']),
				('QXD0013',['QXD0005']),
				('QXD0010',['QXD0001']),
				('QXD0006',['QXD0109']),
				('QXD0008',['QXD0056']),
				
				('QXD0114',['']),
				('QXD0115',['QXD0010']),
				('QXD0040',['QXD0008']),
				('QXD0017',['QXD0008']),
				('QXD0012',['QXD0056']),
				
				('QXD0011',['']),
				('QXD0016',['QXD0007']),
				('QXD0041',['QXD0008', 'QXD0010']),
				('QXD0116',['']),
				('QXD0014',['QXD0007']),
				
				('QXD0025',['QXD0040']),
				('QXD0119',['QXD0116']),
				('QXD0120',['QXD0116']),
				('QXD0021',['']),
				('QXD0020',['QXD0007']),
				
				('QXD0019',['QXD0007']),
				('QXD0038',['']),
				('QXD0043',['QXD0113']),
				('QXD0037',['QXD0017']),
				('QXD0046',['QXD0040']),
				
				('QXD0110',['QXD0046']),
				('QXD0157',['']),
				('QXD0155',['']),
				('QXD0029',['']),
				
				('QXD0158',['QXD0157']),
				('QXD0156',['QXD0155']),
				
				('QXD0187',['']),
				('QXD0175',['']),
				('QXD0174',['']),
				('QXD0173',['']),
				('QXD0035',['']),
				('QXD0036',['QXD0035']),
				('QXD0058',['QXD0014']),
				('QXD0061',['QXD0014']),
				('QXD0060',['QXD0019']),
				('QXD0068',['QXD0019']),
				('QXD0042',['QXD0019']),
				('QXD0023',['QXD0019']),
				('QXD0063',['QXD0019']),
				('QXD0062',['QXD0019']),
				('QXD0069',['QXD0021']),
				('QXD0073',['QXD0019']),
				('QXD0075',['QXD0020']),
				('QXD0090',['QXD0021']),
				('QXD0048',['QXD0021']),
				('QXD0113',['']),
				('QXD0169',['QXD0012']),
				('QXD0185',['QXD0012']),
				('QXD0167',['QXD0017']),
				('QXD0172',['QXD0017']),
				('QXD0152',['QXD0008']),
				('QXD0181',['QXD0041', 'QXD0120']),
				('QXD0171',['QXD0041', 'QXD0116']),
				('QXD0168',['QXD0041']),
				('QXD0186',['QXD0006', 'QXD0116']),
				('QXD0183',['QXD0013', 'QXD0041']),
				('QXD0177',['QXD0041']),
				('QXD0076',['QXD0007']),
				('QXD176',['QXD0012', 'QXD0041']),
				('QXD0178',['QXD0012', 'QXD0011', 'QXD0041']),
				('QXD0179',['QXD0012']),
				('QXD018',['QXD0011']),
				('QXD0170',['QXD0041']),
				('QXD0188',['QXD0119']),
				('QXD0182',['QXD0119']),
				('QXD0184',['QXD0119']),
				('QXD0044',['']),
				('QXD0078',['QXD0020']),
				('QXD0134',['QXD0006']),
				('QXD0180',['QXD0006']),
				('QXD0099',['QXD0007', 'QXD0011']),
				('QXD0153',['QXD0041']),
				('PRG0002',['']),
				('PRG0003',['']),
				('PRG0004',['']),
				]

ofertaDisciplina = [('QXD0108',t,1),
					('QXD0001',t,1),
					('QXD0005',t,1),
					('QXD0056',t,1),
					('QXD0103',t,1),
					('QXD0109',t,1),
					
					('QXD0007',t,2),
					('QXD0013',t,2),
					('QXD0010',t,2),
					('QXD0006',t,2),
					('QXD0008',t,2),
					
					('QXD0114',t,3),
					('QXD0115',t,3),
					('QXD0040',t,3),
					('QXD0017',t,3),
					('QXD0012',t,3),
					
					('QXD0011',t,4),
					('QXD0016',t,4),
					('QXD0041',t,4),
					('QXD0116',t,4),
					('QXD0014',t,4),
					
					('QXD0025',t,5),
					('QXD0119',t,5),
					('QXD0120',t,5),
					('QXD0021',t,5),
					('QXD0020',t,5),
					
					('QXD0019',t,6),
					('QXD0038',t,6),
					('QXD0043',t,6),
					('QXD0037',t,6),
					('QXD0046',t,6),
					
					('QXD0110',t,7),
					('QXD0157',t,7),
					('QXD0155',t,7),
					('QXD0029',t,7),
					
					('QXD0158',t,8),
					('QXD0156',t,8),
					
					('QXD0187',f,zero),
					('QXD0175',f,zero),
					('QXD0174',f,zero),
					('QXD0173',f,zero),
					('QXD0035',f,zero),
					('QXD0036',f,zero),
					('QXD0058',f,zero),
					('QXD0061',f,zero),
					('QXD0060',f,zero),
					('QXD0068',f,zero),
					('QXD0042',f,zero),
					('QXD0023',f,zero),
					('QXD0063',f,zero),
					('QXD0062',f,zero),
					('QXD0069',f,zero),
					('QXD0073',f,zero),
					('QXD0075',f,zero),
					('QXD0090',f,zero),
					('QXD0048',f,zero),
					('QXD0113',f,zero),
					('QXD0169',f,zero),
					('QXD0185',f,zero),
					('QXD0167',f,zero),
					('QXD0172',f,zero),
					('QXD0152',f,zero),
					('QXD0181',f,zero),
					('QXD0171',f,zero),
					('QXD0168',f,zero),
					('QXD0186',f,zero),
					('QXD0183',f,zero),
					('QXD0177',f,zero),
					('QXD0076',f,zero),
					('QXD176',f,zero),
					('QXD0178',f,zero),
					('QXD0179',f,zero),
					('QXD018',f,zero),
					('QXD0170',f,zero),
					('QXD0188',f,zero),
					('QXD0182',f,zero),
					('QXD0184',f,zero),
					('QXD0044',f,zero),
					('QXD0078',f,zero),
					('QXD0134',f,zero),
					('QXD0180',f,zero),
					('QXD0099',f,zero),
					('QXD0153',f,zero),
					('PRG0002',f,zero),
					('PRG0003',f,zero),
					('PRG0004',f,zero),
					]



def getIdDisciplinaByCodigo(codigo):
	c.execute("SELECT id AS idd FROM disciplina WHERE codigo = %s",[codigo])
	id_disciplina = c.fetchone()
	return (id_disciplina['idd'])


def inserirDisciplina():
	c.executemany('INSERT INTO disciplina (codigo,nome,carga_horaria) VALUES (%s,%s,%s)',disciplinas)
	con.commit()


def inserirCurso():
	cursos = [('404','CIÊNCIA DA COMPUTAÇÃO - QUIXADÁ - PRESENCIAL - BACHARELADO - MT')]
	c.executemany('INSERT INTO curso (codigo,nome) VALUES (%s,%s)',cursos)
	con.commit()


def inserirCurriculo():
	c.execute("SELECT id AS idc FROM curso WHERE codigo = '404'")
	id_curso = c.fetchone()
	idc = id_curso['idc']

	curriculos = [('2013.1',idc)]
	
	c.executemany('INSERT INTO curriculos (codigo,curso_id) VALUES (%s,%s)',curriculos)
	con.commit()

def inserirPreRequisitos():
	codigo_curriculo = '2013.1'
	c.execute("SELECT id AS idc FROM curriculos WHERE codigo = %s",[codigo_curriculo])
	id_curriculo = c.fetchone()
	idc = id_curriculo['idc']
	idc = idc,
	
	for i in range(0,len(preRequisitos)):
		preRequisitos[i] = idc + preRequisitos[i]

		pre_requisitos = preRequisitos[i][2]
		idd = getIdDisciplinaByCodigo(preRequisitos[i][1])
		for j in range(0,len(pre_requisitos)):
			if not pre_requisitos[j] == '':
				#c.execute("SELECT id_disciplina AS idp FROM disciplina WHERE codigo = %s",[pre_requisitos[j]])
				#id_pr = c.fetchone()
				#idp = id_pr['idp']
				idp = getIdDisciplinaByCodigo(pre_requisitos[j])
				pr = [(preRequisitos[i][0],idd,idp)]
				c.executemany('INSERT INTO pre_requisitos (curriculo_id,disciplina_id,disciplina_pre_requisito_id) VALUES (%s,%s,%s)',pr)
				con.commit()

def inserirOfertaDisciplina():
	codigo_curriculo = '2013.1'
	c.execute("SELECT id AS idc FROM curriculos WHERE codigo = %s",[codigo_curriculo])
	id_curriculo = c.fetchone()
	idc = id_curriculo['idc']
	idc = idc,

	for i in range(0,len(ofertaDisciplina)):
		ofertaDisciplina[i] = ofertaDisciplina[i] + idc
		
		idd = getIdDisciplinaByCodigo(ofertaDisciplina[i][0])
		
		carater = ofertaDisciplina[i][1]
		semestre = ofertaDisciplina[i][2]
		curriculo = ofertaDisciplina[i][3]
		oferta = [(idd,carater,semestre,curriculo)]
		
		c.executemany('INSERT INTO oferta_disciplina (disciplina_id,obrigatoria,semestre,curriculo_id) VALUES (%s,%s,%s,%s)',oferta)
		con.commit()





def main():
	#inserirCurso()
	
	#inserirCurriculo()
	
	inserirDisciplina()
	
	inserirPreRequisitos()

	inserirOfertaDisciplina()

	

if __name__ == "__main__":
    main()
