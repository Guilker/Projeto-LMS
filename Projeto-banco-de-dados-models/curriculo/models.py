from django.db import models

class Coordenador (models.Model):
	login = models.CharField("Login", max_length=45)
	senha = models.CharField("Senha", max_length=30)
	nome = models.CharField("Nome", max_length=120)
	email = models.CharField("Email", max_length=80)
	celular= models.CharField("Celular", max_length=11)
	DtExpiração = models.DateField("DtExpiração", default= "01/01/1900",auto_now = False, auto_now_add = False)
	
	def __srt__(self):
		return self.nome
		
class Aluno (models.Model):
	login = models.CharField("Login", max_length=45)
	senha = models.CharField("Senha", max_length=30)
	nome = models.CharField("Nome", max_length=120)
	email = models.CharField("Email", max_length=80)
	celular= models.CharField("Celular", max_length=11)
	DtExpiração = models.DateField("DtExpiração", default= "01/01/1900",auto_now = False, auto_now_add = False)
	ra = models.IntegerField("RA")
	foto = models.CharField("Foto", max_length=255) 
	
	def __srt__(self):
		return self.nome

class Aluno (models.Model):
	login = models.CharField("Login", max_length=45)
	senha = models.CharField("Senha", max_length=30)
	nome = models.CharField("Nome", max_length=120)
	email = models.CharField("Email", max_length=80)
	celular= models.CharField("Celular", max_length=11)
	DtExpiração = models.DateField("DtExpiração", default= "01/01/1900",auto_now = False, auto_now_add = False)
	ra = models.IntegerField("RA")
	
	def __srt__(self):
		return self.nome

class Disciplina (models.Model):
	nome = models.CharField("Nome", max_length=45)
	data = models.DateField("Data")
	status = models.CharField("Status", max_length=50, default= "Aberta")
	PlanoEnsino = models.CharField("PlanoEnsino", max_length=120)
	CargaHorario = models.IntegerField("CargaHoraria")
	competencia = models.CharField("Competencias", max_length=200)
	habilidades = models.CharField("Habilidades", max_length=200)
	emenda = models.CharField("Emenda", max_length=200)
	ConteudoProgramatico = models.CharField("ConteudoProgramatico",max_length= 200 )
	PercentualPratico = models.DecimalField("PercentualPratico", max_digits=4, decimal_places=2)
	PercentualTeorico = models.DecimalField("PercentualTeorico", max_digits=4, decimal_places=2)
	
	def __srt__(self):
		return self.nome

class Curso (models.Model):
	nome = models.CharField("Nome", max_length=45)
	
	def __srt__(self):
		return self.nome

class DisciplinaOfertada (models.Model):
	DtInicioMatricula2 = models.DateField("DtInicioMatricula2")
	DtFimMatricula2 = models.DateField("DtFimMatricula2")
	Ano = models.CharField("Ano", max_length=4)
	Semestre = models.CharField("Semestre", max_length=2)
	Turma = models.CharField("Turma", max_length=1)
	Metodologia = models.CharField("Metodologia", max_length=200)
	Recursos = models.CharField("Recursos", max_length=200)
	CriterioAvaliacao = models.CharField("CriterioAvaliacao", max_length=200)
	PlanoDeAulas = models.CharField("PlanoDeAulas", max_length=200)

	
	def __srt__(self):
		return self.nome	
		
class SolicitacaoMatricula (models.Model):
	DtSolicitacao = models.DateField("DtSolicitacao")
	status = models.CharField("Status", max_length=50, default= "Solicitada")
	
	def __srt__(self):
		return self.nome	

class DisciplinaOfertada (models.Model):
	Descricao = models.CharField("Descricao", max_length=200)
	Conteudo = models.CharField("Conteudo", max_length=200)
	Tipo = models.CharField("Tipo", max_length=200)
	Extras = models.CharField("Extras", max_length=200)

	
	def __srt__(self):
		return self.nome


class AtividadeVinculada (models.Model):
	Rotulo = models.CharField("Rotulo", max_length=120)
	Status = models.CharField("Status", max_length=200)
	DtInicioRespostas = models.DateField("DtInicioRespostas")
	DtFimRespostas = models.DateField("DtFimRespostas")


	
	def __srt__(self):
		return self.nome


class DisciplinaOfertada (models.Model):
	Titulo = models.CharField("Titulo", max_length=200)
	Resposta = models.CharField("Resposta", max_length=200)
	DtEntrega = models.DateField("DtEntrega")
	Status = models.CharField("Status", max_length=120, default = "Entregue")
	Nota = models.DecimalField("Nota", max_digits=4, decimal_places=2)
	Obs = models.CharField("Obs", max_length=120)
	
	
	def __srt__(self):
		return self.nome		
	


class Mensagem (models.Model):
	Assunto = models.CharField("Assunto", max_length=100)
	Referencia = models.CharField("Referencia", max_length=120)
	Conteudo = models.CharField("Conteudo", max_length=100)
	Status = models.CharField("Status", max_length=100)
	DtEnvio = models.DateField("DtEnvio")
	DtResposta = models.DateField("DtResposta")
	Resposta = models.CharField("Resposta", max_length=200)


	
	def __srt__(self):
		return self.nome	

"""class Curso (models.Model):
	nome = models.CharField ("Nome", max_length=50)

	def __str__(self):
		return self.nome
		

class Coordenador (models.Model):
	login = models.CharField("Login", max_length=45)
	senha = models.CharField("Senha", max_length=30)
	nome = models.CharField("Nome", max_length=120)
	email = models.CharField("Email", max_length=80)
	celular= models.CharField("Celular", max_length=11)
	DtExpiração = models.DateField("DtExpiração", default= "01/01/1900",auto_now = False, auto_now_add = False)
	
	def __srt__(self):
		return self.nome

class Aluno (models.Model):
	login = models.CharField("Login", max_length=45)
	senha = models.CharField("Senha", max_length=30)
	nome = models.CharField("Nome", max_length=120)
	email = models.CharField("Email", max_length=80)
	celular= models.CharField("Celular", max_length=11)
	DtExpiração = models.DateField("DtExpiração", default= "01/01/1900",auto_now = False, auto_now_add = False)
	ra = models.IntegerField("RA")
	foto = models.CharField("Foto", max_length=255) 
	
	def __srt__(self):
		return self.nome
		
		
class Disciplina (models.Model):
	nome = models.CharField("Nome", max_length=45)
	data = models.DateField("Data")
	status = models.CharField("Status", max_length=50, default= "Aberta")
	PlanoEnsino = models.CharField("PlanoEnsino", max_length=120)
	CargaHorario = models.IntegerField("CargaHoraria")
	competencia = models.CharField("Competencias", max_length=200)
	habilidades = models.CharField("Habilidades", max_length=200)
	emenda = models.CharField("Emenda", max_length=200)
	ConteudoProgramatico = models.CharField("ConteudoProgramatico",max_length= 200 )
	PercentualPratico = models.DecimalField("PercentualPratico", max_digits=4, decimal_places=2)
	PercentualTeorico = models.DecimalField("PercentualTeorico", max_digits=4, decimal_places=2)
	
	def __srt__(self):
		return self.nome"""	

		
				

