from ajudante import Ajudante

class SeletorDeModos(object):

    def setModo(self, modo):
        """Função responsável por setar o modo de tranmissao de dados.
        """
        sinaldo.setValor(modo)
        if modo == 0 or modo == 1:
            tempo.setTransmissao(False)
            altitudePressao.setTransmissao(False)
            wow.setTransmissao(False)
            velCas.setTransmissao(False)
            pressaoEstaticar.setTransmissao(False)
            pressaoTotalr.setTransmissao(False)
            rpmD.setTransmissao(False)
            posicaoX.setTransmissao(False)
            posicaoY.setTransmissao(False)
            altitude.setTransmissao(False)
            rpmE.setTransmissao(False)
            taxaGiroX.setTransmissao(False)
            taxaGiroY.setTransmissao(False)
            taxaGiroZ.setTransmissao(False)
            aceleracaoX.setTransmissao(False)
            aceleracaoY.setTransmissao(False)
            aceleracaoZ.setTransmissao(False)
            pitch.setTransmissao(False)
            roll.setTransmissao(False)
            pressaoEstatica.setTransmissao(False)
            pressaoTotal.setTransmissao(False)
            temperaturaBar.setTransmissao(False)
            densidadeAr.setTransmissao(False)
            altitudeRelativa.setTransmissao(False)
            dadoTempoGPS.setTransmissao(False)
            latitude.setTransmissao(False)
            longitude.setTransmissao(False)
            direcaoCurso.setTransmissao(False)
            velocidade.setTransmissao(False)
            velocidadeSubida.setTransmissao(False)
            erroX.setTransmissao(False)
            erroY.setTransmissao(False)
            erroAltitude.setTransmissao(False)
            erroVelocidade.setTransmissao(False)
            erroVelocidadeSubida.setTransmissao(False)
            latitudeRef.setTransmissao(False)
            longitudeRef.setTransmissao(False)
            distanciaAbsoluta.setTransmissao(False)
            pressADC.setTransmissao(False)
            pressTensao.setTransmissao(False)
            pressaoDin.setTransmissao(False)
            wowRaw.setTransmissao(False)
            tempoVoo.setTransmissao(False)
            distancia.setTransmissao(False)
            distRef.setTransmissao(False)
            sinaldo.setTransmissao(True)
            nivelFixacao.setTransmissao(True)
            agravante.setTransmissao(True)
            ultimoTransmitido.setTransmissao(False)
        # 2 = Apenas transmitindo tempo, Vcas, HP, RPM e altitude(gps)
        elif modo == 2:
            tempo.setTransmissao(True)
            altitudePressao.setTransmissao(True)
            wow.setTransmissao(True)
            velCas.setTransmissao(True)
            pressaoEstaticar.setTransmissao(False)
            pressaoTotalr.setTransmissao(False)
            rpmD.setTransmissao(True)
            posicaoX.setTransmissao(False)
            posicaoY.setTransmissao(False)
            altitude.setTransmissao(True)
            rpmE.setTransmissao(True)
            taxaGiroX.setTransmissao(False)
            taxaGiroY.setTransmissao(False)
            taxaGiroZ.setTransmissao(False)
            aceleracaoX.setTransmissao(False)
            aceleracaoY.setTransmissao(False)
            aceleracaoZ.setTransmissao(False)
            pitch.setTransmissao(True)
            roll.setTransmissao(True)
            pressaoEstatica.setTransmissao(False)
            pressaoTotal.setTransmissao(False)
            temperaturaBar.setTransmissao(False)
            densidadeAr.setTransmissao(False)
            altitudeRelativa.setTransmissao(False)
            dadoTempoGPS.setTransmissao(False)
            latitude.setTransmissao(False)
            longitude.setTransmissao(False)
            direcaoCurso.setTransmissao(False)
            velocidade.setTransmissao(False)
            velocidadeSubida.setTransmissao(False)
            erroX.setTransmissao(False)
            erroY.setTransmissao(False)
            erroAltitude.setTransmissao(False)
            erroVelocidade.setTransmissao(False)
            erroVelocidadeSubida.setTransmissao(False)
            latitudeRef.setTransmissao(False)
            longitudeRef.setTransmissao(False)
            distanciaAbsoluta.setTransmissao(False)
            pressADC.setTransmissao(False)
            pressTensao.setTransmissao(False)
            pressaoDin.setTransmissao(False)
            wowRaw.setTransmissao(False)
            tempoVoo.setTransmissao(False)
            distancia.setTransmissao(False)
            distRef.setTransmissao(False)
            sinaldo.setTransmissao(True)
            nivelFixacao.setTransmissao(True)
            agravante.setTransmissao(True)
            ultimoTransmitido.setTransmissao(False)
        elif (modo == 3) or (modo == 4):
            tempo.setTransmissao(True)
            altitudePressao.setTransmissao(True)
            wow.setTransmissao(True)
            velCas.setTransmissao(True)
            pressaoEstaticar.setTransmissao(True)
            pressaoTotalr.setTransmissao(True)
            rpmD.setTransmissao(True)
            posicaoX.setTransmissao(True)
            posicaoY.setTransmissao(True)
            altitude.setTransmissao(True)
            rpmE.setTransmissao(True)
            taxaGiroX.setTransmissao(False)
            taxaGiroY.setTransmissao(False)
            taxaGiroZ.setTransmissao(False)
            aceleracaoX.setTransmissao(False)
            aceleracaoY.setTransmissao(False)
            aceleracaoZ.setTransmissao(False)
            pitch.setTransmissao(True)
            roll.setTransmissao(True)
            pressaoEstatica.setTransmissao(False)
            pressaoTotal.setTransmissao(False)
            temperaturaBar.setTransmissao(False)
            densidadeAr.setTransmissao(False)
            altitudeRelativa.setTransmissao(False)
            dadoTempoGPS.setTransmissao(False)
            latitude.setTransmissao(False)
            longitude.setTransmissao(False)
            direcaoCurso.setTransmissao(False)
            velocidade.setTransmissao(False)
            velocidadeSubida.setTransmissao(False)
            erroX.setTransmissao(False)
            erroY.setTransmissao(False)
            erroAltitude.setTransmissao(False)
            erroVelocidade.setTransmissao(False)
            erroVelocidadeSubida.setTransmissao(False)
            latitudeRef.setTransmissao(False)
            longitudeRef.setTransmissao(False)
            distanciaAbsoluta.setTransmissao(False)
            pressADC.setTransmissao(False)
            pressTensao.setTransmissao(False)
            pressaoDin.setTransmissao(False)
            wowRaw.setTransmissao(False)
            tempoVoo.setTransmissao(False)
            distancia.setTransmissao(False)
            distRef.setTransmissao(False)
            sinaldo.setTransmissao(True)
            nivelFixacao.setTransmissao(True)
            agravante.setTransmissao(True)
            ultimoTransmitido.setTransmissao(False)