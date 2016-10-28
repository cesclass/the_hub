# coding: UTF-8
#
#-------------------------------------------------------------------
# 
#                               Code (Type) : python 3.x        
#           ____                Fichier     : the_hub.py        
#          / __ \__  __         Projet      : THE HUB           
#         / /_/ / / / /         Creation    : 08.10.2016        
#        / ____/ /_/ /          Mise a Jour : 24.10.2016        
#       /_/    \__, /           Developpeur : Cyril ESCLASSAN 
#             /____/            Version     : 1.1 BETA               
#                               Systeme     : W10 CMD
#                               Copyright   : GPL v3             
# 
#-------------------------------------------------------------------
#                 _____ _  _ ___   _  _ _   _ ___                   
#                |_   _| || | __| | || | | | | _ )                  
#                  | | | __ | _|  | __ | |_| | _ \                  
#                  |_| |_||_|___| |_||_|\___/|___/                  
#                                                                   
#-------------------------------------------------------------------
#
#   THE HUB est un programme qui centralise toutes les fonctions 
#   utiles créés depuis le début de l'initiation au langage python.
#
#   THE HUB peut aussi contenir des fonctions en BETA TEST
#
#   Ce programme va évoluer en fonction des semaines/mois
#
#   Sources : https://github.com/cesclass/the_hub
#   Contact : @cynex294 sur Twitter
#
#-------------------------------------------------------------------
#   JOURNAL NOTES
#
#   08.10.2016 - 18.10.2016
#   + Debut du projet THE HUB
#   + Presentation (en tête) fini
#   + Squelette du programme terminé
#   + Le proto fonctionne, tout est vide donc tout reste a faire
#   + Retrais d'éléments innutiles, optimisations...
#   + Retrais de la fonction lcd_err(), chaque fonctions devra gerer 
#   ses propres erreurs d'elle meme.
#   + Proto IHM CMD : OK
#   + Gestion d'erreurs main() : OK
#   + An egg was appear...
#
#   19.10.2016
#   + Mise en place d'une zone journal et notes #MyLife
#   + Remplissage des jours passés rétroactivement avec les notes
#   prisent en cour de route
#   + OUI ! L'utilisation de lcd() est innutile mais j'avais
#   envie, alors faites pas chier ! (^_^)
#   + ok, mes yeux brules, la chasse aux instructions sans ';' est ouverte
#   + ça y est le code est en 'prod', Yann l'a tester et c'est cool ^^
#
#   21.10.2016
#   + Corrections de queslques fautes dans le texte du programme
#   + Suppression de vieilles constantes innutiles
#   + Conversion des consts systeme en lambda
#
#   23.10.2016
#   + Reprise du code, il y a des choses qui ne vont pas
#   + Changement du menu main, passage de la selection par lettres à
#   la selection par chiffre / nombre
#   + Changement des conditions d'anti erreurs
#   + Le 'egg' passe dans le switch case et le exit remonte pour
#   prendre sa place
#
#   24.10.2016
#   + 2:10 Ajout de la fonction d'addition binaire (fonctionnelle) 
#   + Constatation, le code manque cruellement de commentaire
#   + Remplacement des .__len__() par len()
#-------------------------------------------------------------------

# import

from random import randrange;
from os import system;
from math import ceil;
from time import sleep;

#-------------------------------------------------------------------

# id function for lcd()
LCD_MAIN  = 'main';
LCD_FACTO = 'facto';
LCD_BIX   = 'bix';
LCD_OROUL = 'roulette';
LCD_EGG   = 'egg';
LCD_INFO  = 'info';
LCD_BIN   = 'addbin';

# Systeme...
sys_title = lambda: system('title THE HUB');
sys_theme = lambda: system('color 3f'); # sys-theme... MDR ! (^_^)
sys_pause = lambda: system('pause > nul');
sys_clear = lambda: system('cls');
sys_size  = lambda: system('mode con cols=52 lines=22');


#-------------------------------------------------------------------

# lcd(display : str, n : int) : bool

def lcd(display = '', n = 0):

    sys_clear();

    if(display is LCD_MAIN):
        print(' +------------------------------------------------+');
        print(' |       _____ _  _ ___   _  _ _   _ ___          |');
        print(' |      |_   _| || | __| | || | | | | _ )         |');
        print(' |        | | | __ | _|  | __ | |_| | _ \         |');
        print(' |        |_| |_||_|___| |_||_|\___/|___/         |');
        print(' |                                                |');
        print(' +------------------------------------------------+');
        print('                                      [Q]: Quitter ');
        print('                                                   ');
        print(' [1]: Informations sur le programme                ');
        print(' [2]: Verificateur d\'annee Bissextile             ');
        print(' [3]: Fonction Factorielle !(x)                    ');
        print(' [4]: Jeu de l\'openRoulette                       ');
        print(' [5]: Addition binaire (0b + 0b)                   ');
        print(' [ ]: D\'autres choses soon...                     ');
        print('                                                   ');
        return True;

    elif(display is LCD_BIX):
        print(' +------------------------------------------------+');
        print(' |  ___ ___ ___ ___ _____  _______ ___ _    ___   |');
        print(' | | _ )_ _/ __/ __| __\ \/ /_   _|_ _| |  | __|  |');
        print(' | | _ \| |\__ \__ \ _| >  <  | |  | || |__| _|   |');
        print(' | |___/___|___/___/___/_/\_\ |_| |___|____|___|  |');
        print(' |                                                |');
        print(' +------------------------------------------------+');
        print('                                      [Q]: Quitter ');
        print('                                                   ');
        return True;

    elif(display is LCD_FACTO):
        print(' +------------------------------------------------+');
        print(' |   ___ _   ___ _____ ___  ___ ___   _   _       |');
        print(' |  | __/_\ / __|_   _/ _ \| _ \_ _| /_\ | |      |');
        print(' |  | _/ _ \ (__  | || (_) |   /| | / _ \| |__    |');
        print(' |  |_/_/ \_\___| |_| \___/|_|_\___/_/ \_\____|   |');
        print(' |                                                |');
        print(' +------------------------------------------------+');
        print('                                      [Q]: Quitter ');
        print('                                                   ');
        return True;

    elif(display is LCD_OROUL):
        print(' +------------------------------------------------+');
        print(' |    ___  ___  _   ___    ___ _____ _____ ___    |');
        print(' |   | _ \/ _ \| | | | |  | __|_   _|_   _| __|   |');
        print(' |   |   / (_) | |_| | |__| _|  | |   | | | _|    |');
        print(' |   |_|_\\\___/ \___/|____|___| |_|   |_| |___|   |');
        print(' |                                                |');
        print(' +------------------------------------------------+');
        print('                                      [Q]: Quitter ');
        print('                                                   ');
        print(' Vous avez', n, 'jetons  '); # Taille de 'n' inconnue
        print('                                                   ');
        return True;

    elif(display is LCD_BIN):
        print(' +------------------------------------------------+');
        print(' |         ___ ___ _  _      _   ___  ___         |');
        print(' |        | _ )_ _| \| |    /_\ |   \|   \        |');
        print(' |        | _ \| || .` |   / _ \| |) | |) |       |');
        print(' |        |___/___|_|\_|  /_/ \_\___/|___/        |');
        print(' |                                                |');
        print(' +------------------------------------------------+');
        print('                                      [Q]: Quitter ');
        print('                                                   ');
        print(' [ENTER]: Resultat precedent                       ');
        print('                                                   ');
        return True;

    elif(display is LCD_INFO):
        print(' +------------------------------------------------+');
        print(' |            ___ _  _ ___ ___  ___               |');
        print(' |           |_ _| \| | __/ _ \/ __|              |');
        print(' |            | || .` | _| (_) \__ \              |');
        print(' |           |___|_|\_|_| \___/|___/              |');
        print(' |                                                |');
        print(' +------------------------------------------------+');
        print('                                                   ');
        print('   Programme         : THE HUB (v1.1 BETA)         ');
        print('   Mise à Jour       : 24.10.2016                  ');
        print('   Systèmes          : W7, 8, 10 x86_64            ');
        print('                                                   ');
        print('   Dev-Langage       : Python3.x                   ');
        print('   Doc-Langage       : FR-French                   ');
        print('                                                   ');
        print('   Concept et Dev    : Cyril ESCLASSAN             ');
        print('   Contact           : @cynex294 - Twitter         ');
        print('                                                   ');
        print('   Sources github    : cesclass/the_hub/           ');
        print('   Licence           : GPL v3                      ');
        print('                                                   ');
        return True;

    elif(display is LCD_EGG):
        print('                                                   ');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42       42 42 42 42 42 42                42 42');
        print(' 42 42       42 42 42 42 42 42                42 42');
        print(' 42 42       42 42 42 42 42 42 42 42 42       42 42');
        print(' 42 42       42 42 42 42 42 42 42 42 42       42 42');
        print(' 42 42       42       42 42 42                42 42');
        print(' 42 42       42       42 42 42                42 42');
        print(' 42 42                   42 42       42 42 42 42 42');
        print(' 42 42                   42 42       42 42 42 42 42');
        print(' 42 42 42 42 42       42 42 42                42 42');
        print(' 42 42 42 42 42       42 42 42                42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        print(' 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42');
        return True;

    else:
        return False;

#-------------------------------------------------------------------

# bissextile(none) : bool

def bissextile():
    
    while(True): # Oui, c'est une boucle infine, je veux rien savoir, barrez vous !
        
        lcd(LCD_BIX);
        print(' Saisir l\'annee à vérifier');
        annee = input(' > ');

        if(annee.upper() == 'Q'): # Exit
            break;

        try: 
            annee = int(annee);
        
        except ValueError:
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        if(bix_core(annee)):
            print(' L\'année:', annee, 'est bissextile.');
        else:
            print(' L\'année:', annee, 'n\'est pas bissextile.');

        sys_pause();

# bist_core work function of bissextile

# bix_core(n : int) : bool

def bix_core(n):

    # Si l'annee n est un multiple de 400 OU un multiple de 4
    # sans etre un multiple de 100, l'annee est bissextile
    if( n%400 == 0 or (n%4 == 0 and n%100 != 0) ):
        return True;
    else:
        return False;

#-------------------------------------------------------------------

# factorielle(none) : bool

def factorielle():

    while(True): # Encore un while true...

        lcd(LCD_FACTO);
        print(' Saisir un nombre a mettre en factorielle');
        nombre = input(' > ');

        if(nombre.upper() == 'Q'): # Exit
            break;

        try: 
            nombre = int(nombre);
        
        except ValueError:
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        print(' !(' + str(nombre) + ') =', facto_core(nombre));

        sys_pause();

# facto_core work function of factorielle

# facto_core(n : int) : string

def facto_core(n):

    result = n; 
    n -= 1;

    for i in range(n - 1):  # n - 1 : multiple par 1 innutile
        result *= n;
        n -= 1;

    sResult = str(result);
    len_sResult = len(sResult);

    if(len_sResult > 12):
        sCutResult = sResult[0] + '.';
        for e in range(1, 6):
            sCutResult += sResult[e];
        sCutResult += 'e' + str(len_sResult - 1);
        return sCutResult;

    return sResult;

#-------------------------------------------------------------------

# openRoulette(none) : bool

def openRoulette():
    coins = 1000;
    turn = 0;

    while(coins > 0):

        lcd(LCD_OROUL, coins);

        print(' Choisissez un numero entre 0 et 49 ');
        num = input(' > ');

        if(num.upper() == 'Q'):
            break;

        try:
            num = int(num);
            assert(num <= 49 and num >= 0);

        except ValueError:
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        except AssertionError:
            print(' E: Le numero saisie est hors', 
                'des limites : [0-49]');
            sys_pause();
            continue;

        print(' Saisir la somme a miser ');
        mise = input(' > ');

        try:
            mise = int(mise);
            assert(mise <= coins and mise > 0);

        except ValueError:
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        except AssertionError:
            print(' E: La somme misée n\'est pas valide'); 
            sys_pause();
            continue;

        turn += 1;
        coins -= mise;
        gain = 0;
        win = randrange(50);
        win_color = "";
        num_color = "";

        if(win%2 == 0):
            win_color = 'noir';
        else:
            win_color = 'rouge';

        if(num%2 == 0):
            num_color = 'noir';
        else:
            num_color = 'rouge';
        
        print('');
        print(' Vous avez misé', mise, 'jetons sur le',
            num, num_color);
        print('');
        print(' Le numero gagnant est le', win, win_color);

        if(win == num):
            gain = 3*mise;
            print(' Bravo, vous avez gagné', gain, 'jetons (^_^)');

        elif(win_color == num_color):
            gain = ceil(mise/2);
            print(' Bravo, vous avez récupéré', gain, 'jetons (°_°)');

        else:
            print(' Oups, vous avez perdu', mise, 'jetons (-_-)');

        coins += gain;

        sys_pause();

    lcd(LCD_OROUL, coins);
    if(coins == 0):
        print(' Vous avez perdu... (-_-)');
    if(turn > 0):
        print(' Vous avez joué', turn, 'fois');
        print(' Merci d\'avoir joué à l\'openRoulette');
        sys_pause();

#-------------------------------------------------------------------

# additionBinaire(none) : bool

def additionBinaire():
    
    num1 = ''
    num2 = ''
    nbin_add = ''

    while(True):
        lcd(LCD_BIN);

        print(' Saisissez le premier nombre en binaire');
        num1 = input(' > ');

        if(num1 == ''):
            num1 = nbin_add.replace(' ', '');

        if(num1.upper() == 'Q'):
            break;

        elif(not num1.isnumeric()):
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        try:
            for i in range(len(num1)):
                assert(num1[i] == '0' or num1[i] == '1');
        except AssertionError:
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        print('')
        print(' Saisissez le second nombre en binaire');
        num2 = input(' > ');

        if(num2 == ''):
            num2 = nbin_add.replace(' ', '');

        if(not num2.isnumeric()):
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        try:
            for i in range(len(num2)):
                assert(num2[i] == '0' or num2[i] == '1');
        except AssertionError:
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        nbin_add, nbin_1, nbin_2 = add_bin_core(num1, num2);
        print('');
        print(' .', nbin_1, '\n +', nbin_2, '\n =', nbin_add);
        sys_pause();


# add_bin_core work function of additionBinaire

# add_bin_core(nbin_1 : str, nbin_2 : str) : str, str, str

# La fonction add_bin_core prend en parametres deux strings 
# contenant des chiffres (0 et 1 uniquement).
# Elle retourne le resultat de l'addition et les strings pris en
# parametre dans une version modifié pour l'affichage de nombres binaires

def add_bin_core(nbin_1, nbin_2):
    # reverse str
    nbin_1 = ''.join(reversed(nbin_1));
    nbin_2 = ''.join(reversed(nbin_2));

    addition = '';
    lePlusGrand = '';
    turn = 0;
    supp = 0;
    retenu = False

    if(len(nbin_1) == len(nbin_2)):
        turn = len(nbin_1);
    elif(len(nbin_1) < len(nbin_2)):
        turn = len(nbin_1);
        supp = len(nbin_2);
        lePlusGrand = nbin_2;
    else:
        turn = len(nbin_2);
        supp = len(nbin_1);
        lePlusGrand = nbin_1;


    for i in range(turn):
        if(nbin_1[i] == '0' and nbin_2[i] == '0'):
            if(retenu):
                addition += '1';
                retenu = False;
            else :
                addition += '0';

        elif(nbin_1[i] == '1' and nbin_2[i] == '1'):
            if(retenu):
                addition += '1';
            else:
                addition += '0';
            retenu = True;

        else:
            if(retenu):
                addition += '0';
            else:
                addition += '1';

    if(supp != 0):
        for i in range(turn, supp):
            if(lePlusGrand[i] == '0'):
                if(retenu):
                    addition += '1';
                    retenu = False;
                else :
                    addition += '0';
            else:
                if(retenu):
                    addition += '0';
                    retenu = True;
                else:
                    addition += '1';

    if(retenu):
        addition += '1';

    retourAdd = '';
    retourBin1 = '';
    retourBin2 = '';

    # Separation tous les 4 chiffres
    for i in range(len(addition)):
        if(i%4 == 0 and i != 0):
            retourAdd += ' ';
        retourAdd += addition[i];

    for i in range(len(nbin_1)):
        if(i%4 == 0 and i != 0):
            retourBin1 += ' ';
        retourBin1 += nbin_1[i];

    for i in range(len(nbin_2)):
        if(i%4 == 0 and i != 0):
            retourBin2 += ' ';
        retourBin2 += nbin_2[i];

    # Ajout d'espaces pour l'allignement de la presentation
    if(len(retourBin1) > len(retourBin2)):
        for i in range(len(retourBin2), len(retourBin1)):
            retourBin2 += ' ';

    elif(len(retourBin1) < len(retourBin2)):
        for i in range(len(retourBin1), len(retourBin2)):
            retourBin1 += ' ';

    if(len(retourBin1) < len(retourAdd)):
        for i in range(len(retourBin1), len(retourAdd)):
            retourBin1 += ' ';

    if(len(retourBin2) < len(retourAdd)):
        for i in range(len(retourBin2), len(retourAdd)):
            retourBin2 += ' ';

    # re-reverse str
    retourAdd = ''.join(reversed(retourAdd));
    retourBin1 = ''.join(reversed(retourBin1));
    retourBin2 = ''.join(reversed(retourBin2));

    return retourAdd, retourBin1, retourBin2;

#-------------------------------------------------------------------

# setScreen(none) : bool

def setScreen():

    sys_size();
    sys_theme();
    sys_title();
    sys_clear();
    
    return True;

#-------------------------------------------------------------------

# egg(none) : none

def egg():
    lcd(LCD_EGG)

    temps = 0
    cycle = 0.125   # 40 * 0.125 = 5.0s
                    # 1 tour = 8*0.125
                    # 5.0s = 5 tours
    color = 'color 0'

    system('title 42')

    while(temps < 5):
        for i in range(8, 16): 
            # system('color 0' + 0x(i) - "0x" )
            system(color + hex(i).replace("0x", "") );
            sleep(cycle);
            temps += cycle;

    setScreen();

#-------------------------------------------------------------------

# main(none) : none

def main():
    setScreen();
    select = "";

    while(True):

        lcd(LCD_MAIN);
        select = input(' > ');

        # Exit
        if(select.upper() == 'Q'):
            print('\n Merci d\'avoir utilisé THE HUB. (^_^)');
            sys_pause();
            sys_clear();
            break;

        # Bloc anti erreurs
        try:
            select = int(select);
        except ValueError:
            print(' E: La saisie est incorrecte');
            sys_pause();
            continue;

        # Switch Case, appel de fonctions
        if(select == 42):   # Egg
            egg();

        elif(select == 1):  # Informations
            lcd(LCD_INFO);      
            sys_pause();

        elif(select == 2):  # Bissextile
            bissextile();

        elif(select == 3):  # Factorielle
            factorielle();

        elif(select == 4):  # OpenRoulette
            openRoulette();

        elif(select == 5):  # AdditionBinaire
            additionBinaire();

        else:   # select != 1 OU 2 OU 3 OU 4 OU 5
            print(' E: La saisie est incorrecte');
            sys_pause();
            
    return 0;
    # end

#-------------------------------------------------------------------

if(__name__ == '__main__'):
    main();
