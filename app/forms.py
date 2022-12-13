from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired



class DadosUsuario(FlaskForm):
    genero = RadioField( 'genero',choices=['Masculino','Feminino'], validators=[DataRequired()])
    comunicacao = RadioField('comunicacao',choices=['Quase Sempre','Raramente','Sempre','Nunca' ], validators=[DataRequired()])
    repetitivos = RadioField( 'repetitivos',choices=['Quase Sempre','Raramente','Sempre','Nunca' ], validators=[DataRequired()])
    social = RadioField('social',choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    fala = RadioField('fala', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    olhos = RadioField('olhos', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    risos = RadioField( 'risos', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    carinho = RadioField( 'carinho', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    relacionamento = RadioField( 'relacionamento', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    brinquedos = RadioField( 'brinquedos', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    nao_verbal = RadioField( 'nao_verbal', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    monotona = RadioField( 'monotona', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    pergunta = RadioField( 'pergunta', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    expressao = RadioField( 'expressao', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    perigo = RadioField( 'perigo', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    tempo = RadioField( 'tempo', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    balanca = RadioField( 'balanca', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    rotina = RadioField( 'rotina', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    agitado = RadioField( 'agitado', choices=['Quase Sempre','Raramente','Sempre','Nunca'], validators=[DataRequired()])
    
    

    submit = SubmitField('Enviar')

