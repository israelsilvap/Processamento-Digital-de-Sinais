# Prática 2 de Processamento Digital de Sinais

## Descrição do Projeto
Este projeto faz parte da disciplina de **Processamento Digital de Sinais** (ECO077) da Universidade Federal do Ceará, Campus Sobral. O objetivo principal desta prática é aplicar técnicas de **filtragem de áudio** para a remoção de ruídos em sinais de áudio utilizando MATLAB. A seguir, é apresentado um resumo das atividades realizadas:

### Etapas Realizadas

1. **Carregamento do Sinal de Áudio**
   - O arquivo de áudio **botao.wav** foi carregado utilizando a função `audioread` do MATLAB. O sinal de áudio foi analisado no domínio do tempo, com a visualização de sua forma de onda.

2. **Transformada de Fourier do Sinal de Áudio**
   - A **Transformada de Fourier** foi aplicada ao sinal de áudio para observar seu espectro de frequências. O gráfico da magnitude da FFT foi gerado, permitindo a análise das componentes espectrais do áudio.

3. **Adição de Ruído Branco Gaussiano**
   - Foi adicionado um **ruído branco gaussiano** ao sinal de áudio, com média zero e variância igual a 1. O sinal ruidoso foi visualizado tanto no domínio do tempo quanto no domínio da frequência, mostrando o impacto do ruído nas altas frequências.

4. **Design do Filtro Passa-Baixas**
   - Um **filtro passa-baixas** de ordem 6 foi projetado utilizando o método de **Butterworth**, com uma **frequência de corte de 2 kHz**. A resposta ao impulso, a resposta em magnitude (em dB) e a resposta em fase do filtro foram geradas para análise.

5. **Aplicação do Filtro ao Sinal Ruidoso**
   - O filtro passa-baixas foi aplicado ao sinal ruidoso para **remover as altas frequências**. O gráfico do sinal filtrado foi gerado, mostrando a **atenuação do ruído** e a **preservação do sinal original**.

6. **Transformada de Fourier do Sinal Filtrado**
   - A **Transformada de Fourier** do sinal filtrado foi calculada para visualizar a mudança no espectro de frequências após a aplicação do filtro. O gráfico mostrou uma redução significativa nas frequências mais altas, onde o ruído estava concentrado.

7. **Escuta do Sinal Filtrado**
   - O sinal filtrado foi **reproduzido** para ouvir a **qualidade melhorada** do áudio, com o **ruído reduzido**. A resposta subjetiva foi documentada, observando-se a **diminuição do ruído** sem perda significativa do conteúdo do sinal original.

8. **Diagrama de Polos e Zeros do Filtro**
   - O **diagrama de polos e zeros** do filtro foi gerado para visualizar o comportamento do filtro no plano complexo. O gráfico confirmou que o filtro era de fato um **filtro passa-baixas** com boa performance na **remoção do ruído de alta frequência**.

## Conclusão
Esta prática permitiu a aplicação de técnicas de **filtragem de áudio** para a remoção de **ruído branco** utilizando um **filtro passa-baixas** de **Butterworth**. A análise espectral e o diagrama de polos e zeros ajudaram a entender o comportamento do filtro. A adição de ruído e a subsequente filtragem reforçaram a importância dos filtros na **remoção de ruídos indesejados** em sinais de áudio. A prática também demonstrou a eficácia de **filtros passa-baixas** na **preservação do sinal útil** ao mesmo tempo que **reduzem o ruído nas altas frequências**.
