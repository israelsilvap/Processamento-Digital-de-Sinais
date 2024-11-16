#Prática 1 de Processamento Digital de Sinais

## Descrição do Projeto
Este projeto faz parte da disciplina de Processamento Digital de Sinais (ECO077) da Universidade Federal do Ceará, Campus Sobral. O objetivo principal desta prática é aplicar conceitos de geração, análise e filtragem de sinais digitais utilizando MATLAB. A seguir, é apresentado um resumo das atividades realizadas:

### Etapas Realizadas

1. **Geração do Sinal**
   - Foi gerado um sinal composto pela soma de três funções seno com frequências angulares de 0,1π, 0,5π e 0,75π rad/s, e amplitudes correspondentes de 1, 1.5 e 0.5. O sinal contém 100 amostras e foi plotado em um gráfico.

2. **Transformada de Fourier do Sinal**
   - A Transformada de Fourier foi aplicada ao sinal gerado para visualizar o seu espectro de frequências. O eixo de frequências variou de -π a π e o gráfico do módulo da FFT foi plotado.

3. **Filtro Butterworth**
   - Um filtro passa-baixa de ordem 4, com frequência de corte de 0,3π rad/s, foi projetado usando o filtro de Butterworth. Foi gerada também a resposta ao impulso do filtro.

4. **Resposta em Magnitude do Filtro**
   - A resposta em magnitude do filtro Butterworth foi analisada e o gráfico correspondente foi gerado para visualizar como o filtro se comporta ao longo das frequências entre -π e π.

5. **Filtragem do Sinal**
   - O sinal original foi filtrado usando o filtro Butterworth. O gráfico do sinal filtrado foi gerado para observar os efeitos da filtragem no domínio do tempo.

6. **Transformada de Fourier do Sinal Filtrado**
   - A Transformada de Fourier do sinal filtrado foi calculada para entender como o espectro de frequências foi alterado após a filtragem. O gráfico mostra a supressão de componentes de alta frequência.

7. **Adição de Ruído Branco**
   - Um ruído branco gaussiano, com média zero e variância de 0,1, foi adicionado ao sinal original. As etapas de geração, Transformada de Fourier, filtragem e análise do sinal foram repetidas utilizando este sinal ruidoso, e os gráficos resultantes foram gerados para comparação.

## Conclusão
Esta prática permitiu explorar a geração e manipulação de sinais no domínio do tempo e da frequência, além de entender os efeitos da filtragem utilizando um filtro passa-baixa. A adição de ruído e a análise subsequente reforçaram a importância dos filtros na remoção de ruídos indesejados.
