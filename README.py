#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar/usar o `opemfoam` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para instalar/configurar/usar o `opemfoam` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to install/configure/use the `opemfoam` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `OpemFOAM`
# 
# O `OpenFOAM` é um software de código aberto utilizado para simulação de dinâmica de fluidos computacional (CFD - Computational Fluid Dynamics), que permite modelar e analisar o comportamento de fluidos e outros fenômenos físicos complexos. Ele é usado em várias indústrias, como engenharia automotiva, aeroespacial, de energia e de construção naval, para simulações de escoamento de fluidos, transferência de calor, reações químicas e muito mais. O `OpenFOAM` é altamente flexível e personalizável, permitindo aos usuários adaptar o software às suas necessidades específicas e desenvolver novos modelos e algoritmos.
# 
# ### `ParaView`
# 
# O `ParaView` é uma plataforma de visualização de dados de código aberto, amplamente utilizada para análise e visualização de grandes volumes de dados científicos, como os gerados em simulações numéricas e experimentos. Ele é especialmente eficaz em processar e representar dados 3D de forma interativa, oferecendo uma vasta gama de ferramentas e filtros para manipulação e exibição de informações complexas. O ParaView suporta múltiplos formatos de dados e pode ser executado em sistemas de alto desempenho, permitindo a visualização de dados em larga escala, como os utilizados em engenharia, física, biologia e outras áreas científicas. Além disso, o ParaView possui uma interface gráfica intuitiva e pode ser estendido por scripts Python, o que o torna uma ferramenta altamente flexível para pesquisadores e engenheiros.
# 
# ### `gmsh`
# 
# O `GMSH` é um software de código aberto usado para geração de malhas (meshes) 3D, amplamente utilizado em simulações numéricas, especialmente em métodos de elementos finitos (FEM). Ele permite criar, visualizar e modificar malhas de alta qualidade para representar geometrias complexas em diversas áreas, como engenharia, física e simulações científicas. O GMSH suporta várias dimensões e tipos de elementos, como tetraedros e hexaedros, e oferece ferramentas avançadas para gerar malhas estruturadas ou não estruturadas. Além disso, o GMSH inclui um visualizador interativo que permite a inspeção detalhada das malhas, facilitando o processo de preparação para simulações e análise de dados. Ele também pode ser integrado com outros softwares de simulação, tornando-se uma parte crucial do fluxo de trabalho de modelagem e análise computacional.
# 
# ### `docker`
# 
# O `Docker` é uma plataforma de código aberto que automatiza o processo de desenvolvimento, implantação e execução de aplicativos dentro de contêineres. Um contêiner é uma unidade leve e isolada que empacota um aplicativo e suas dependências, permitindo que ele seja executado de maneira consistente em qualquer ambiente, seja em um servidor local ou na nuvem. O Docker facilita a criação, distribuição e execução de aplicativos, proporcionando maior flexibilidade e escalabilidade, além de resolver problemas comuns de "funciona na minha máquina". Ele é amplamente utilizado em ambientes de DevOps e CI/CD (integração e entrega contínuas) devido à sua eficiência e capacidade de garantir que os aplicativos sejam executados de forma idêntica em diferentes sistemas.
# 
# ### `cfMesh`
# 
# O `cfMesh` é uma ferramenta de malhagem (mesh generation) para simulações de dinâmica de fluidos computacional (CFD) que integra bem com o OpenFOAM. Ele é projetado para criar malhas 3D de alta qualidade, com foco em geometria complexa e aplicações de CFD, facilitando a geração de malhas para simulações de escoamento de fluidos e outras análises físicas. O cfMesh é conhecido por sua capacidade de lidar com geometrias complexas, oferecendo flexibilidade na criação de malhas estruturadas e não estruturadas. Ele também possui uma interface amigável e é capaz de gerar malhas de forma eficiente, tornando-se uma ferramenta essencial para engenheiros e pesquisadores que trabalham com simulações numéricas avançadas.
# 
# ### `HiSA`
# 
# O `HiSA` (Hierarchical Simulation Architecture) é uma ferramenta de simulação usada para modelagem e análise de sistemas complexos, particularmente em áreas como simulação numérica e modelagem de sistemas dinâmicos. Ele oferece uma estrutura hierárquica para a criação e organização de simulações, permitindo aos usuários modelar sistemas com múltiplas camadas e interações entre componentes. O HiSA é útil em contextos como engenharia, física e outras disciplinas que requerem a simulação de processos complexos, pois facilita a construção de modelos mais detalhados e a análise de seus comportamentos sob diferentes condições.
# 
# 

# ## 1. Configurar/Instalar/Usar o `OpemFOAM` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `OpemFOAM` no `Linux Ubuntu`, você pode usar o gerenciador de pacotes apt. Siga os passos abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# ## 1. Instalação o `OpemFOAM` no `Linux Ubuntu` via Repositório Oficial do `OpenFOAM` (Recomendado)
# 
# Para instalar o `OpemFOAM` no `Linux Ubuntu` pelo `Terminal Emulator`, você pode seguir os passos abaixo. Para obter a versão mais recente diretamente da fonte.
# 
# 1. **Remover versões antigas do `OpenFOAM`**
# 
#     Antes de instalar a nova versão, remova qualquer versão anterior para evitar conflitos:
# 
#     ```
#     sudo apt remove --purge 'openfoam*' -y
#     sudo rm -rf /usr/lib/openfoam
#     sudo rm -rf /opt/openfoam*
#     sudo rm -rf /var/lib/dpkg/info/openfoam*
#     ```
# 
# 2. Agora, atualize os pacotes:
# 
#     ```
#     sudo apt update
#     ```
# 
# 3. **Adicionar o repositório do `OpenFOAM`**:
# 
#     ```
#     sudo sh -c "wget -O - https://dl.openfoam.com/add-debian-repo.sh | bash"
#     ```
# 
# 4. **Atualizar a lista de pacotes**:
# 
#     ```
#     sudo apt update
#     ```
# 
# 3. **Instalar a versão desejada**:
# 
#     ```
#     sudo apt install openfoam2312-default -y
#     ```
# 
#     Caso precise de uma versão específica, verifique qual está disponível:
# 
#     ```
#     apt-cache search openfoam
#     ```
# 
#     E instale a desejada, por exemplo:
# 
#     ```
#     sudo apt install openfoam2406-default -y
#     ```
# 

# ### 1.1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `OpemFOAM` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há
#     ```

# ### 1.1 Verificar se a Instalação Foi Bem-Sucedida
# 
# Após a instalação, verifique se o `OpenFOAM` está no diretório correto:
# 
# ```
# ls -al /usr/lib/openfoam
# ls -al /usr/bin | grep openfoam
# ```
# 
# Se os arquivos existirem, a instalação foi concluída corretamente.

# ### 1.2 Configurar o `OpenFOAM` para Carregar Sempre
# 
# 1. Agora, carregue o `OpenFOAM` corretamente no terminal. Para garantir que isso aconteça automaticamente sempre que abrir o `Terminal Emulator`, adicione ao `~/.bashrc` (ou `~/.zshrc` se usar Zsh):
# 
#     * Para `Bash`, use:
# 
#     ```
#     echo "source /usr/lib/openfoam/etc/bashrc" >> ~/.bashrc
#     source ~/.bashrc
#     ```
# 
#     * Para `Zsh`, use:
# 
#     ```
#     echo "source /usr/lib/openfoam/openfoam2312/etc/bashrc" >> ~/.zshrc
#     source ~/.zshrc
#     ```
# 
# 2. Altere para a pasta do `OpenFOAM`:
# 
#     ```
#     cd /usr/lib/openfoam/openfoam2312
#     ```
# 
# 3. Agora, teste se o `wmake` funciona:
# 
#     ```
#     which wmake
#     ```
# 
# Se `wmake` aparecer corretamente, a instalação está funcionando!

# ### 1.3 Testar a instalação
# 
# 1. Depois de carregar corretamente o ambiente do OpenFOAM, teste com:
# 
#     ```
#     foamInstallationTest
#     ```
# 
# 2. E verifique a versão instalada:
# 
#     ```
#     foamVersion
#     ```
# 

# ## 2. Instalação o `docker` no `Linux Ubuntu` (Opcional, mas recomendado)
# 
# Para instalar o `Docker` no `Linux Ubuntu`, siga os passos abaixo:
# 
# 1. **Criar diretório para armazenar a chave GPG e adicionar a chave**:
# 
#     ```
#     sudo mkdir -p /etc/apt/keyrings
#     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.gpg > /dev/null
#     sudo chmod a+r /etc/apt/keyrings/docker.gpg
#     ```
# 
# 2. **Adicionar o repositório oficial do `Docker`**
# 
#     ```
#     echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
#     https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#     ```
# 
# 3. **Atualizar os pacotes e instalar o `Docker`**
# 
#     ```
#     sudo apt update
#     sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
#     ```
# 
# 4. **Habilitar e iniciar o serviço `Docker`**
# 
#     ```
#     sudo systemctl enable docker
#     sudo systemctl start docker
#     ```
# 
# 5. **Verificar se o `Docker` está rodando corretamente**:
# 
#     ```
#     sudo systemctl status docker
#     ```
# 
# 6. **Permitir uso sem `sudo` (Opcional, mas recomendado):**
# 
#     ```
#     sudo usermod -aG docker $USER
#     echo "Reinicie ou faça logout para aplicar as permissões"
#     ```
# 
# 7. **Testar a instalação com um container de exemplo**:
# 
#     ```
#     docker run hello-world
#     ```

# ## 3. Instalação o `ParaView` no `Linux Ubuntu` (Opcional, mas recomendado)
# 
# Para obter a versão mais recente diretamente da página oficial do `ParaView`.
# 
# 1. **Instalação via Binário Oficial (Recomendado)**:
# 
#     ```
#     sudo apt install paraview -y
#     ```
# 
# 2. **Testar a instalação**:
# 
#     ```
#     paraview
#     ```
# 
# **Dicas Extras**
# 
# * Se o `ParaView` não abrir, verifique se você tem uma GPU compatível e drivers atualizados:
# 
#     ```
#     glxinfo | grep "OpenGL version"
#     ```
# 
# * Para verificar a versão instalada:
# 
#     ```
#     paraview --version
#     ```
# 
# * Se estiver rodando no WSL (Windows Subsystem for Linux), pode precisar de um servidor gráfico como `X11` ou `VcXsrv`.
# 

# ## 4. Instalação o `gmsh` no `Linux Ubuntu`
# 
# Se você deseja uma instalação rápida e está satisfeito com a versão disponível nos repositórios do `Ubuntu`, use:
# 
# 1. **Digite no `Terminal Emulator` o comando**:
# 
#     ```
#     sudo apt install gmsh -y
#     ```
# 
# **Desvantagem**: Pode não ser a versão mais recente.
# 
# 2. **Para verificar a versão instalada**:
# 
#     ```
#     gmsh --version
#     ```
# 
# 3. **Abrir o `Gmsh` com Interface Gráfica (GUI)**:
# 
# Se você instalou o `Gmsh` corretamente, pode abrir a interface gráfica com o seguinte comando no terminal:
# 
# ```
# gmsh
# ```
# 
# Se a instalação estiver correta, a interface do `Gmsh` será exibida.
# 
# Alternativamente, você também pode procurar `"Gmsh"` no menu de aplicativos do seu ambiente gráfico (`XFCE`, `GNOME`, `KDE` etc.).

# ## 5. Instalação o `cfMesh` no `Linux Ubuntu` 
# 
# O `cfMesh` é um gerador de malha para `OpenFOAM` e pode ser instalado de diferentes formas no `Ubuntu`. Aqui estão os principais métodos de instalação:
# 
# ### 5.1 **Instalando o `cfMesh` a partir do `OpenFOAM`**:
# 
# Se você já tem o `OpenFOAM` instalado, pode verificar se o `cfMesh` já está incluído na sua versão.
# 
# 1. **Verifique se o `cfMesh` está disponível**:
# 
#     ```
#     ls $FOAM_UTILITIES/mesh/generation/cfMesh
#     ```
# 
#     Se o diretório existir, significa que o `cfMesh` já está instalado no `OpenFOAM`.
# 
# 2. **Para rodar um teste**:
# 
#     ```
#     cartesianMesh -help
#     ```
# 
# Se o comando for reconhecido, então o `cfMesh` está funcionando corretamente.
# 

# ### 5.2 Instalando o `cfMesh` Manualmente
# 
# Se o `cfMesh` não estiver incluído na sua versão do `OpenFOAM`, você pode baixá-lo e compilá-lo manualmente.
# 
# 1. **Verificar o Caminho da Pasta ThirdParty Diretamente**:
# 
#     Tente rodar este comando para verificar onde a variável `$WM_THIRD_PARTY_DIR` está definida:
# 
#     ```
#     echo $WM_THIRD_PARTY_DIR
#     ```
# 
#     * Se retornar um caminho, você pode navegar até ele com:
# 
#         ```
#         cd $WM_THIRD_PARTY_DIR
#         ls -al
#         ```
# 
#     * Se o comando não retornar nada, siga os próximos passos para localizar a pasta.
# 
#         1.1 Verificar se existe algum arquivo `ThirdParty`, pois se existir, você deverá excluí-lo com o comando:
# 
#         ```
#         sudo rm -rf /usr/lib/openfoam/openfoam2312/ThirdParty
#         ```
# 
#         1.2 **Crie o Diretório `ThirdParty` Novamente**:
# 
#         ```
#         sudo mkdir /usr/lib/openfoam/openfoam2312/ThirdParty
#         ls -al
#         ```
# 
#         Ajuste as permissões para o seu usuário poder escrever no diretório:
# 
#         ```
#         sudo chown -R $USER:$USER /usr/lib/openfoam/openfoam2312/ThirdParty
#         ls -al
#         ```
# 
# 2. Definindo Permanentemente (Persistente em Todas as Sessões). Se você quer que a variável esteja sempre disponível:
# 
#     2.1. **Adicione ao `.bashrc` ou `.zshrc`**:
# 
#     * **Se usa `Bash`**:
# 
#         ```
#         echo 'export WM_THIRD_PARTY_DIR=/usr/lib/openfoam/openfoam2312/ThirdParty' >> ~/.bashrc
#         source ~/.bashrc
#         ```
# 
#     * **Se usa `Zsh` (Z shell)**:
# 
#         ```
#         echo 'export WM_THIRD_PARTY_DIR=/usr/lib/openfoam/openfoam2312/ThirdParty' >> ~/.zshrc
#         source ~/.zshrc
#         ```
# 
# 3. **Verifique**:
#     
#         ```
#         echo $WM_THIRD_PARTY_DIR
#         ```
# 
# 4. **Navegue até a pasta de terceiros do `OpenFOAM`**:
# 
#     ```
#     cd $WM_THIRD_PARTY_DIR
#     ```
# 
#     ou
# 
#     ```
#     cd /usr/lib/openfoam/openfoam2312/ThirdParty
#     ```
# 
# 5. **Baixar o `cfMesh`**:
# 
#     ```
#     sudo git clone https://develop.openfoam.com/Community/integration-cfmesh.git
#     ```
# 
# 6. Depois, corrija as permissões para que seu usuário possa compilar o código:
# 
#     ```
#     sudo chown -R $USER:$USER /usr/lib/openfoam/openfoam2312/ThirdParty/integration-cfmesh
#     ls -al
#     ```
# 
# 7. Agora tente acessar a pasta:
# 
#     ```
#     cd /usr/lib/openfoam/openfoam2312/ThirdParty/integration-cfmesh
#     ```
# 
# 8. **Configurar o ambiente**:
# 
#     ```
#     source $FOAM_ETC/bashrc
#     ```
# 
# 9. **Compilar o `cfMesh`**:
# 
#     ```
#     source $WM_PROJECT_DIR/etc/bashrc
#     sudo -E bash -c "source /usr/lib/openfoam/openfoam2312/etc/bashrc
#     ./Allwclean
#     ./Allwmake -j$(nproc)"
#     ```
# 
#     Isso pode levar alguns minutos, dependendo do seu processador.
# 
# 10. **Verificar se a instalação foi bem-sucedida**:
# 
#     ```
#     cartesianMesh -help
#     ```
# 
#     Se o comando for reconhecido, a instalação foi concluída com sucesso!
# 

# #### Verificar se as variáveis ambiente estão definidas corretamente
# 
# 1. **Executar o comando**:
# 
#     ```
#     echo $FOAM_INST_DIR
#     echo $FOAM_RUN
#     echo $FOAM_TUTORIALS
#     echo $PV_PLUGIN_PATH
#     echo $WM_THIRD_PARTY_DIR
#     echo $WM_PROJECT_USER_DIR
#     ```
# 
#     * Se cada um dos comandos retornar um diretório, as variáveis ambiente estão definidas e corretas.
# 
#     * Se algum dos comandos **NÃO** retornar um diretório, por exemplo, o `$FOAM_INST_DIR` e o `$WM_PROJECT_USER_DIR`, será necessário incluir no `Terminal`, como segue:
# 
#         * Para `Bash`:
# 
#             ```
#             export FOAM_INST_DIR=/usr/lib/openfoam
#             export WM_PROJECT_USER_DIR=/home/$USER$/OpenFOAM
#             echo 'export FOAM_INST_DIR=/usr/lib/openfoam' >> ~/.bahrc
#             source ~/.bashrc
#             ```
# 
#         * Para `Z Shell`:
# 
#             ```
#             export FOAM_INST_DIR=/usr/lib/openfoam
#             export WM_PROJECT_USER_DIR=/home/$USER$/OpenFOAM
#             echo 'export FOAM_INST_DIR=/usr/lib/openfoam' >> ~/.zshrc
#             source ~/.zshrc
#             ```
# 
#             * Agora, teste novamente:
# 
#             ```
#             echo $FOAM_INST_DIR
#             echo $WM_PROJECT_USER_DIR
#             ```
# 
#             Se aparecer `/usr/lib/openfoam` e `/home/$USER$/OpenFOAM`, o problema foi resolvido.
# 

# #### 5.2.1 Verificando a instalação dos executáveis
# 
# Após instalar, verifique se os executáveis do `cfMesh` estão disponíveis:
# 
# ```
# which cartesianMesh
# which tetMesh
# which polyDualMesh
# ```
# 
# Se os caminhos forem retornados corretamente, significa que o `cfMesh` está pronto para uso.
# 

# #### 5.2.2 Testando o `cfMesh` com um Caso de Exemplo
# 
# Você pode rodar um exemplo simples para testar se o `cfMesh` está funcionando corretamente. Se a malha for gerada corretamente, o `cfMesh` está pronto para uso.
# 
# 1. **Preparar o Ambiente**: Ative o `OpenFOAM` e configure o ambiente:
# 
#     ```
#     source /usr/lib/openfoam/openfoam2312/etc/bashrc
#     ```
# 
# 2. **Criar Diretório de Teste**:
# 
#     ```
#     sudo mkdir -p $FOAM_RUN/cfmesh_test
#     cd $FOAM_RUN/cfmesh_test
#     ```
# 
# 3. **Copiar os Tutoriais do cfMesh**: Os tutoriais estão em `/usr/lib/openfoam/openfoam2312/ThirdParty/integration-cfmesh/tutorials/`:
# 
#     Copie o exemplo `cartesianMesh` para o diretório de teste:
# 
#     ```
#     sudo cp -r /usr/lib/openfoam/openfoam2312/ThirdParty/integration-cfmesh/tutorials/cartesianMesh .
#     ```
# 
# 4. **Verifique se o diretório foi copiado corretamente**: Execute o comando abaixo para verificar se o diretório `asmoOctree` está no local esperado:
# 
#     ```
#     ls -al ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/cartesianMesh/
#     ```
# 
#     Se o diretório `asmoOctree` não aparecer, significa que o exemplo não foi copiado corretamente.
# 
#     4.1 **(Re)Copiar o diretório de exemplo**: Caso o diretório não esteja presente, recopie o exemplo usando:
# 
#     ```
#     sudo cp -r /usr/lib/openfoam/openfoam2312/ThirdParty/integration-cfmesh/tutorials/cartesianMesh ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/
#     ```
# 
#     Verifique novamente com:
# 
#     ```
#     ls -al ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/cartesianMesh/
#     ```
# 
# 5. **Corrijir as permissões (se necessário)**: Se o diretório existir, mas ainda houver problemas de acesso, ajuste as permissões:
# 
#     ```
#     sudo chown -R $USER:$USER ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test
#     chmod -R u+rwx ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test
#     ```
# 
# 5. **Escolher o Exemplo para Executar**: Por exemplo, vamos usar o `asmoOctree`:
# 
#     ```
#     cd ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/cartesianMesh/asmoOctree
#     ```
# 
# 6. **Agora, execute o comando**:
# 
#     ```
#     cartesianMesh
#     ```
# 
#     Se houver erro de permissão na criação de diretórios (como o `/constant`), use:
# 
#     ```
#     sudo chmod -R u+rwx ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/cartesianMesh/asmoOctree
#     ```
# 
#     E depois execute novamente:
# 
#     ```
#     cartesianMesh
#     ```
# 

# #### 5.2.3 Verificar a Malha Criada
# 
# Após a execução bem-sucedida, visualize a malha usando o `paraFoam`:
# 
# 
# 1. **Verifique se o diretório `constant/` existe**: Execute:
# 
#     ```
#     ls -al ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/cartesianMesh/asmoOctree/constant/
#     ```
# 
#     * Se o diretório não existir, crie-o:
# 
#     ```
#     mkdir ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/cartesianMesh/asmoOctree/constant/
#     ```
# 
#     * Se o diretório existir mas estiver **vazio**, isso causará o erro. O diretório deve conter um subdiretório `polyMesh` e outros arquivos essenciais.
# 
# 2. **Verifique as permissões do diretório**: Corrija as permissões para garantir acesso completo:
# 
#     ```
#     sudo chown -R $USER:$USER ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/
#     chmod -R u+rwX ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/
#     ```
# 
# 3. **Verifique se o `polyMesh` foi gerado**: No diretório `constant/`, deve haver um subdiretório `polyMesh` com arquivos como:
# 
#     * `boundary`
# 
#     * `faces`
#     
#     * `meshMetaDict`
#     
#     * `neighbour`
# 
#     * `owner`
# 
#     * `points`
# 
#     Verifique com:
# 
#     ```
#     ls -al ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/cartesianMesh/asmoOctree/constant/polyMesh/
#     ```
# 
#     Se esses arquivos estiverem ausentes, reexecute o `cartesianMesh`:
# 
#     ```
#     cartesianMesh
#     ```
# 
# 4. **(Alternativa) Converter para VTK com `foamToVTK`**: 
# 
# 
#     4.1 Para não ocorrer erro de permissão durante o `foamToVTK`, execute:
# 
#     ```
#     sudo chown -R $USER:$USER ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/
#     ```
#     
#     4.2 Se o erro persistir ou se preferir abrir o caso diretamente no `ParaView`:
# 
#     ```
#     foamToVTK
#     ```
# 
#     * Os arquivos convertidos serão salvos no diretório:
# 
#     ```
#     ~/OpenFOAM/edenedfsls-v2312/run/cfmesh_test/cartesianMesh/asmoOctree/VTK/
#     ```
# 
#     * No `ParaView`, abra o arquivo `asmoOctree_0.vtm`.series para visualizar o caso:
# 
#     ```
#     paraview
#     ```
# 
#     4.3 Dentro do `paraview`, clicar em `Apply`.
# 
# 5. **Corrigir `PV_PLUGIN_PATH` (opcional, mas recomendado)**: Adicione o caminho dos _plugins_ do `ParaView` ao seu ambiente:
# 
#     ```
#     export PV_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/paraview-5.10/plugins
#     ```
# 
#     Adicione essa linha ao seu `~/.zshrc` para manter permanente:
# 
#     ```
#     echo 'export PV_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/paraview-5.10/plugins
#     ' >> ~/.zshrc
#     source ~/.zshrc
#     ```

# ## 5.3 Instalar o `HiSA` (High Speed Aerodynamics)
# 
# O `HiSA` (High Speed Aerodynamics) é um solver de alta velocidade para `OpenFOAM`, especializado em escoamentos compressíveis. Ele não está incluído na distribuição padrão do `OpenFOAM`, então precisa ser instalado manualmente.
# 
# ### 5.3.1 Pré-requisitos
# 
# Antes de instalar o `HiSA`, verifique se você tem o `OpenFOAM` instalado e configurado corretamente.
# 
# 1. **Teste se o `OpenFOAM` está instalado**:
# 
#     ```
#     foamInstallationTest
#     ```
# 
#     Se não estiver instalado, siga os passos desta instalação.
# 

# ### 5.3.2 Baixar o código-fonte do `HiSA`
# 
# O código-fonte do `HiSA` pode ser obtido no `GitLab` do projeto.
# 
# 1️. **Navegue até a pasta do `OpenFOAM`**:
# 
#     ```
#     cd $WM_THIRD_PARTY_DIR
#     ```
# 
#     Se a variável `$WM_THIRD_PARTY_DIR` não retornar nada, ela pode não estar definida, tente:
# 
#     ```
#     cd /usr/lib/openfoam/openfoam2312/ThirdParty
#     ```
# 
# 2. **Baixar o `HiSA` do repositório oficial**:
# 
#     ```
#     sudo git clone https://gitlab.com/hisa/hisa.git
#     ```
# 
# 3️. **Acesse a pasta do `HiSA`**:
# 
#     ```
#     cd hisa
#     ```
# 

# #### 5.3.3 Configurar e Compilar o `HiSA`
# 
# 1. **Configure o ambiente antes da compilação**:
# 
# Se o `OpenFOAM` não estiver ativado, faça:
# 
# ```
# source /usr/lib/openfoam/openfoam2312/etc/bashrc
# export WM_THIRD_PARTY_DIR=/usr/lib/openfoam/openfoam2312/ThirdParty
# ```
# 
# 2. Agora, para garantir que o `HiSA` seja compilado corretamente, verifique as dependências:
# 
# ```
# ./Allclean
# ./Allwmake -j$(nproc)
# ```
# 
# Se houver erro de permissão, tente:
# 
# ```
# sudo -E bash -c "source /usr/lib/openfoam/openfoam2312/etc/bashrc && ./Allclean && ./Allwmake -j$(nproc)"
# ```
# 
# 3. **Verifique se o binário foi gerado corretamente**: Liste o diretório de binários do `HiSA`:
# 
#     ```
#     ls -al ~/OpenFOAM/edenedfsls-v2312/platforms/linux64GccDPInt32Opt/bin/
#     ```
#     
#     Se `hisaFoam`, `hisa` ou `HiSA` estiver lá, continue com o próximo passo.
# 
#     Se o binário não estiver lá, recompile o `HiSA`:
# 
#     ```
#     cd /usr/lib/openfoam/openfoam2312/ThirdParty/hisa
#     ./Allclean
#     ./Allwmake -j$(nproc)
#     ```
# 
# 4. **Adicione o binário ao `PATH`**: Execute, para tornar isso permanente, adicione ao `~/.zshrc`:
# 
#     ```
#     echo 'export PATH=~/OpenFOAM/edenedfsls-v2312/platforms/linux64GccDPInt32Opt/bin:$PATH' >> ~/.zshrc
#     source ~/.zshrc
#     ```
# 
#     Agora, teste novamente:
# 
#     ```
#     which hisa
#     ```
# 
#     Se `hisa` aparecer no `which`, significa que a instalação está correta.
#     

# #### 5.3.4 Testar a Instalação
# 
# 1. Depois de compilar, teste se o `HiSA` está instalado corretamente:
# 
#     ```
#     hisa -help
#     ```
# 
# 2. **Confirme se o `hisa` reconhece o `OpenFOAM`**:
# 
# Para garantir que o ambiente `OpenFOAM` está bem configurado para o `hisa`, execute:
# 
#     ```
#     hisa -version
#     ```
# 
#     Isso deve mostrar a versão do `hisa` e do `OpenFOAM`.
# 
# Se `hisa` for reconhecido e rodar corretamente, significa que a instalação foi bem-sucedida! 

# #### 5.3.5 Executar um Caso de Teste
# 
# Para verificar se tudo funciona corretamente, execute um caso-teste:
# 
# ```
# mkdir -p $FOAM_RUN/hisa_test
# cd $FOAM_RUN/hisa_test
# cp -r $FOAM_TUTORIALS/compressible/hisa/mach5_wedge .
# cd mach5_wedge
# hisaFoam
# ```

# ## 6. Encontrar os executáveis das aplicações para o `FreeCAD`
# 
# 

# ## Referências
# 
# [1] OPENAI. ***Instalação opemfoam ubuntu.*** Disponível em: <https://chatgpt.com/c/67af9ad1-09ec-8002-8552-e371c2edb694> (texto adaptado). ChatGPT. Acessado em: 14/02/2025 14:23.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/02/2025 14:23.
# 
# [3] OPENCFD. ***Openfoam**. Disponível em: <https://www.openfoam.com/>. Acessado em: 24/02/2025 22:53
# 
# [4] DEVELOP OPENFOAM. **Openfoam**. Disponível em: <https://develop.openfoam.com/Development/openfoam/-/wikis/precompiled/>. Acessado em: 24/02/2025 22:54.
# 
# [5] DEVELOP OPENFOAM. **Integration-cfmesh**. Disponível em: <https://develop.openfoam.com/Community/integration-cfmesh>. Acessado em: 24/02/2025 22:56. 
# 
# [6] OPENCFD. **Openfoam: manual pages v1912 - the opensource cfd toolbox - cartesianmesh(1)**. Disponível em: <https://www.openfoam.com/documentation/guides/v1912/man/cartesianMesh.html>. Acessado em : 26/02/2025 09:14.
# 
