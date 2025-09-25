import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class FN_RN_FinanceAnalyzer:
    def __init__(self):
        self.parti = "Front National / Rassemblement National"
        self.colors = ['#000080', '#FF0000', '#8B0000', '#000000', '#FFFFFF', 
                      '#C0C0C0', '#800000', '#003366', '#660000', '#333333']
        
        self.start_year = 1972  # Création du FN
        self.end_year = 2025
        self.creation_year = 1972
        self.renommage_year = 2018  # Devenu Rassemblement National
        
        # Configuration spécifique au FN/RN
        self.config = {
            "type": "parti_politique",
            "orientation": "extreme_droite",
            "electorat_cible": ["ouvriers", "classes_populaires", "ruraux", "patriotes"],
            "budget_base": 8,  # millions d'euros (plus faible que l'UMP initialement)
            "adherents_base": 50000,
            "importance": "croissant",
            "sources_financement": ["cotisations", "dons_petits", "financement_public", "emprunts", "evenements"],
            "specificites": ["financement_controle", "difficultes_bancaires", "soutien_petits_dons"]
        }
        
    def generate_financial_data(self):
        """Génère des données financières pour le FN/RN"""
        print(f"🏛️ Génération des données financières pour {self.parti}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données d'adhérents et structure
        data['Adherents'] = self._simulate_adherents(dates)
        data['Federations_Departementales'] = self._simulate_federations(dates)
        data['Elus_Locaux'] = self._simulate_elus_locaux(dates)
        data['Elus_Nationaux'] = self._simulate_elus_nationaux(dates)
        data['Score_Presidentielles'] = self._simulate_presidential_scores(dates)
        
        # Revenus du parti
        data['Revenus_Total'] = self._simulate_total_revenue(dates)
        data['Cotisations_Adherents'] = self._simulate_membership_fees(dates)
        data['Dons_Petits'] = self._simulate_small_donations(dates)
        data['Dons_Grands'] = self._simulate_large_donations(dates)
        data['Financement_Public'] = self._simulate_public_funding(dates)
        data['Revenus_Evenements'] = self._simulate_event_revenue(dates)
        data['Emprunts'] = self._simulate_loans(dates)
        data['Aides_Etrangeres'] = self._simulate_foreign_aid(dates)
        
        # Dépenses du parti
        data['Depenses_Total'] = self._simulate_total_expenses(dates)
        data['Depenses_Personnel'] = self._simulate_staff_expenses(dates)
        data['Depenses_Campagnes'] = self._simulate_campaign_expenses(dates)
        data['Depenses_Communication'] = self._simulate_communication_expenses(dates)
        data['Depenses_Juridiques'] = self._simulate_legal_expenses(dates)
        data['Depenses_Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Remboursements_Emprunts'] = self._simulate_loan_repayments(dates)
        
        # Indicateurs financiers
        data['Taux_Execution_Budget'] = self._simulate_budget_execution_rate(dates)
        data['Ratio_Cotisations_Revenus'] = self._simulate_membership_ratio(dates)
        data['Dependance_Financement_Public'] = self._simulate_public_funding_dependency(dates)
        data['Solde_Financier'] = self._simulate_financial_balance(dates)
        data['Endettement'] = self._simulate_debt(dates)
        data['Ratio_Depenses_Juridiques'] = self._simulate_legal_ratio(dates)
        
        # Investissements stratégiques
        data['Investissement_Communication'] = self._simulate_communication_investment(dates)
        data['Investissement_Numérique'] = self._simulate_digital_investment(dates)
        data['Investissement_Formation'] = self._simulate_training_investment(dates)
        data['Investissement_International'] = self._simulate_international_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques au FN/RN
        self._add_party_trends(df)
        
        return df
    
    def _simulate_adherents(self, dates):
        """Simule le nombre d'adhérents"""
        base_adherents = self.config["adherents_base"]
        
        adherents = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution historique des adhérents selon les périodes politiques
            if 1972 <= year <= 1980:  # Débuts difficiles
                growth_rate = 0.05
            elif 1981 <= year <= 1987:  # Percée électorale
                growth_rate = 0.15
            elif 1988 <= year <= 1994:  # Consolidation
                growth_rate = 0.08
            elif 1995 <= year <= 2001:  # Présidentielle 1995, 2002
                growth_rate = 0.12
            elif 2002 <= year <= 2006:  # Après 2002
                growth_rate = 0.20
            elif 2007 <= year <= 2010:  # Période intermédiaire
                growth_rate = 0.06
            elif 2011 <= year <= 2016:  # Marine Le Pen
                growth_rate = 0.25
            elif 2017 <= year <= 2021:  # Après 2017
                growth_rate = 0.10
            else:  # 2022-2025
                growth_rate = 0.08
                
            growth = 1 + growth_rate * (i/4)
            noise = np.random.normal(1, 0.10)
            adherents.append(base_adherents * growth * noise)
        
        return adherents
    
    def _simulate_federations(self, dates):
        """Simule le nombre de fédérations départementales"""
        base_federations = 20  # Début modeste
        
        federations = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1980:
                growth_rate = 0.08
            elif year <= 2000:
                growth_rate = 0.12
            elif year <= 2010:
                growth_rate = 0.06
            else:
                growth_rate = 0.10
                
            growth = 1 + growth_rate * (i/5)
            federations.append(base_federations * growth)
        
        return federations
    
    def _simulate_elus_locaux(self, dates):
        """Simule le nombre d'élus locaux"""
        base_elus = 100  # Début très modeste
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections municipales
            if year in [1977, 1983, 1989, 1995, 2001, 2008, 2014, 2020]:
                if year <= 1995:
                    multiplier = 1.3
                elif year <= 2010:
                    multiplier = 1.8
                else:
                    multiplier = 2.2
            else:
                multiplier = 1.0
                
            # Tendance générale de croissance
            if year <= 1990:
                growth_rate = 0.15
            elif year <= 2010:
                growth_rate = 0.20
            else:
                growth_rate = 0.25
                
            growth = 1 + growth_rate * (i/6)
            noise = np.random.normal(1, 0.15)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_elus_nationaux(self, dates):
        """Simule le nombre d'élus nationaux"""
        base_elus = 0  # Aucun élu national au début
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections législatives
            if year in [1973, 1978, 1981, 1986, 1988, 1993, 1997, 2002, 2007, 2012, 2017, 2022]:
                if year == 1986:  # Proportionnelle
                    multiplier = 35
                elif year == 1988:
                    multiplier = 1
                elif year == 1997:
                    multiplier = 1
                elif year == 2002:
                    multiplier = 0
                elif year == 2007:
                    multiplier = 0
                elif year == 2012:
                    multiplier = 2
                elif year == 2017:
                    multiplier = 8
                elif year == 2022:
                    multiplier = 89
                else:
                    multiplier = 0
            else:
                multiplier = 0
                
            # Élections européennes
            if year in [1979, 1984, 1989, 1994, 1999, 2004, 2009, 2014, 2019]:
                europe_multiplier = 3
            else:
                europe_multiplier = 0
                
            total_elus = base_elus + multiplier + europe_multiplier
            elus.append(total_elus)
        
        return elus
    
    def _simulate_presidential_scores(self, dates):
        """Simule les scores présidentiels"""
        scores = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year == 1974:
                score = 0.5
            elif year == 1981:
                score = 0.0  # Pas de candidat
            elif year == 1988:
                score = 14.4
            elif year == 1995:
                score = 15.0
            elif year == 2002:
                score = 16.9
            elif year == 2007:
                score = 10.4
            elif year == 2012:
                score = 17.9
            elif year == 2017:
                score = 21.3
            elif year == 2022:
                score = 41.5
            else:
                score = 0
                
            scores.append(score)
        
        return scores
    
    def _simulate_total_revenue(self, dates):
        """Simule les revenus totaux"""
        base_revenue = self.config["budget_base"]
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Croissance historique des revenus
            if 1972 <= year <= 1980:  # Débuts difficiles
                growth_rate = 0.08
            elif 1981 <= year <= 1987:  # Première percée
                growth_rate = 0.20
            elif 1988 <= year <= 1994:  # Consolidation
                growth_rate = 0.12
            elif 1995 <= year <= 2001:  # Croissance régulière
                growth_rate = 0.15
            elif 2002 <= year <= 2006:  # Après 2002
                growth_rate = 0.25
            elif 2007 <= year <= 2010:  # Période intermédiaire
                growth_rate = 0.10
            elif 2011 <= year <= 2016:  # Marine Le Pen
                growth_rate = 0.30
            elif 2017 <= year <= 2021:  # Après 2017
                growth_rate = 0.18
            else:  # 2022-2025
                growth_rate = 0.22
                
            growth = 1 + growth_rate * (i/4)
            noise = np.random.normal(1, 0.12)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_membership_fees(self, dates):
        """Simule les cotisations des adhérents"""
        base_fees = self.config["budget_base"] * 0.20
        
        fees = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1990:
                growth_rate = 0.10
            elif year <= 2010:
                growth_rate = 0.15
            else:
                growth_rate = 0.20
                
            growth = 1 + growth_rate * (i/5)
            noise = np.random.normal(1, 0.10)
            fees.append(base_fees * growth * noise)
        
        return fees
    
    def _simulate_small_donations(self, dates):
        """Simule les petits dons (spécificité FN/RN)"""
        base_donations = self.config["budget_base"] * 0.35
        
        donations = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Importance croissante des petits dons
            if year <= 1990:
                multiplier = 0.8
            elif year <= 2010:
                multiplier = 1.2
            else:
                multiplier = 1.5
                
            # Cycles électoraux
            if year in [1974, 1988, 1995, 2002, 2007, 2012, 2017, 2022]:
                electoral_multiplier = 2.0
            else:
                electoral_multiplier = 1.0
                
            growth = 1 + 0.08 * (i/3)
            noise = np.random.normal(1, 0.18)
            donations.append(base_donations * growth * multiplier * electoral_multiplier * noise)
        
        return donations
    
    def _simulate_large_donations(self, dates):
        """Simule les grands dons (plus rares pour le FN/RN)"""
        base_donations = self.config["budget_base"] * 0.05
        
        donations = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Difficultés à obtenir des grands dons
            if year <= 2000:
                multiplier = 0.3
            elif year <= 2010:
                multiplier = 0.5
            else:
                multiplier = 0.7
                
            growth = 1 + 0.03 * (i/4)
            noise = np.random.normal(1, 0.25)
            donations.append(base_donations * growth * multiplier * noise)
        
        return donations
    
    def _simulate_public_funding(self, dates):
        """Simule le financement public"""
        base_funding = self.config["budget_base"] * 0.25
        
        funding = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Dépend des résultats électoraux (très variable)
            if year <= 1985:
                multiplier = 0.1  # Très faible
            elif year <= 2000:
                multiplier = 0.4
            elif year <= 2010:
                multiplier = 0.6
            elif year <= 2020:
                multiplier = 0.8
            else:
                multiplier = 1.2  # Augmentation avec les députés
                
            growth = 1 + 0.05 * (i/4)
            noise = np.random.normal(1, 0.15)
            funding.append(base_funding * growth * multiplier * noise)
        
        return funding
    
    def _simulate_event_revenue(self, dates):
        """Simule les revenus des événements"""
        base_revenue = self.config["budget_base"] * 0.08
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1990:
                growth = 1 + 0.06 * max(0, (year - 1990)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.14)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_loans(self, dates):
        """Simule les emprunts (difficultés bancaires spécifiques)"""
        base_loans = self.config["budget_base"] * 0.15  # Plus élevé à cause des difficultés
        
        loans = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Difficultés d'accès au crédit
            if year in [1972, 1984, 1990, 1998, 2005, 2011, 2014, 2020]:
                multiplier = 3.0  # Besoins importants
            else:
                multiplier = 1.0
                
            growth = 1 + 0.04 * (i/4)
            noise = np.random.normal(1, 0.30)  # Forte variabilité
            loans.append(base_loans * growth * multiplier * noise)
        
        return loans
    
    def _simulate_foreign_aid(self, dates):
        """Simule les aides étrangères (controverses)"""
        base_aid = self.config["budget_base"] * 0.02
        
        aid = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2014, 2015, 2016, 2017]:
                multiplier = 2.5  # Période des prêts russes
            else:
                multiplier = 0.5
                
            growth = 1 + 0.01 * (i/4)
            noise = np.random.normal(1, 0.40)  # Très variable
            aid.append(base_aid * growth * multiplier * noise)
        
        return aid
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = self.config["budget_base"] * 0.90
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1974, 1988, 1995, 2002, 2007, 2012, 2017, 2022]:
                multiplier = 1.6  # Années électorales
            else:
                multiplier = 1.0
                
            growth = 1 + 0.06 * (i/3)
            noise = np.random.normal(1, 0.12)
            expenses.append(base_expenses * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_staff_expenses(self, dates):
        """Simule les dépenses de personnel"""
        base_staff = self.config["budget_base"] * 0.25
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2000:
                growth_rate = 0.08
            else:
                growth_rate = 0.12
                
            growth = 1 + growth_rate * (i/4)
            noise = np.random.normal(1, 0.08)
            expenses.append(base_staff * growth * noise)
        
        return expenses
    
    def _simulate_campaign_expenses(self, dates):
        """Simule les dépenses de campagne"""
        base_campaign = self.config["budget_base"] * 0.30
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1974, 1988, 1995, 2002, 2007, 2012, 2017, 2022]:
                multiplier = 4.0  # Campagnes présidentielles
            elif year in [1973, 1978, 1981, 1986, 1988, 1993, 1997, 2002, 2007, 2012, 2017, 2022]:
                multiplier = 2.5  # Législatives
            else:
                multiplier = 0.8
                
            growth = 1 + 0.07 * (i/3)
            noise = np.random.normal(1, 0.28)
            expenses.append(base_campaign * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_communication_expenses(self, dates):
        """Simule les dépenses de communication"""
        base_communication = self.config["budget_base"] * 0.15
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2000:
                growth = 1 + 0.10 * max(0, (year - 2000)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.15)
            expenses.append(base_communication * growth * noise)
        
        return expenses
    
    def _simulate_legal_expenses(self, dates):
        """Simule les dépenses juridiques (spécificité FN/RN)"""
        base_legal = self.config["budget_base"] * 0.08  # Élevé à cause des nombreux procès
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1990, 1998, 2004, 2011, 2015, 2018]:
                multiplier = 2.5  # Périodes de procès importants
            else:
                multiplier = 1.2
                
            growth = 1 + 0.05 * (i/4)
            noise = np.random.normal(1, 0.22)
            expenses.append(base_legal * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        base_operating = self.config["budget_base"] * 0.10
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            growth = 1 + 0.04 * (i/4)
            noise = np.random.normal(1, 0.07)
            expenses.append(base_operating * growth * noise)
        
        return expenses
    
    def _simulate_loan_repayments(self, dates):
        """Simule les remboursements d'emprunts"""
        base_repayment = self.config["budget_base"] * 0.12  # Élevé à cause des difficultés
        
        repayments = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2000:
                growth = 1 + 0.09 * max(0, (year - 2000)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.18)
            repayments.append(base_repayment * growth * noise)
        
        return repayments
    
    def _simulate_budget_execution_rate(self, dates):
        """Simule le taux d'exécution du budget"""
        rates = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1990:
                base_rate = 0.78  # Gestion moins professionnelle
            elif year <= 2010:
                base_rate = 0.82
            else:
                base_rate = 0.86  # Amélioration
                
            noise = np.random.normal(1, 0.06)
            rates.append(base_rate * noise)
        
        return rates
    
    def _simulate_membership_ratio(self, dates):
        """Simule le ratio cotisations/revenus"""
        ratios = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1990:
                base_ratio = 0.25
            elif year <= 2010:
                base_ratio = 0.22
            else:
                base_ratio = 0.28  # Augmentation avec la base militante
                
            noise = np.random.normal(1, 0.06)
            ratios.append(base_ratio * noise)
        
        return ratios
    
    def _simulate_public_funding_dependency(self, dates):
        """Simule la dépendance au financement public"""
        dependencies = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1990:
                base_dependency = 0.15  # Faible (peu d'élus)
            elif year <= 2010:
                base_dependency = 0.25
            elif year <= 2020:
                base_dependency = 0.35
            else:
                base_dependency = 0.45  # Augmentation avec les députés
                
            noise = np.random.normal(1, 0.08)
            dependencies.append(base_dependency * noise)
        
        return dependencies
    
    def _simulate_financial_balance(self, dates):
        """Simule le solde financier"""
        balances = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1974, 1988, 1995, 2002, 2007, 2012, 2017, 2022]:
                base_balance = -0.25  # Déficits électoraux importants
            elif year in [1975, 1989, 1996, 2003, 2008, 2013, 2018, 2023]:
                base_balance = 0.05  # Redressement
            else:
                base_balance = -0.08  # Difficultés chroniques
                
            noise = np.random.normal(1, 0.15)
            balances.append(base_balance * noise)
        
        return balances
    
    def _simulate_debt(self, dates):
        """Simule l'endettement"""
        base_debt = self.config["budget_base"] * 0.3
        
        debt = []
        current_debt = base_debt
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1974, 1984, 1990, 1998, 2005, 2011, 2014, 2020]:
                change_rate = 0.35  # Forte augmentation
            elif year in [1980, 1992, 2000, 2008, 2016, 2022]:
                change_rate = -0.12  # Réduction
            else:
                change_rate = 0.08  # Augmentation régulière
                
            current_debt *= (1 + change_rate)
            noise = np.random.normal(1, 0.12)
            debt.append(current_debt * noise)
        
        return debt
    
    def _simulate_legal_ratio(self, dates):
        """Simule le ratio des dépenses juridiques"""
        ratios = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1990:
                base_ratio = 0.06
            elif year <= 2010:
                base_ratio = 0.09
            else:
                base_ratio = 0.07  # Légère baisse
                
            noise = np.random.normal(1, 0.10)
            ratios.append(base_ratio * noise)
        
        return ratios
    
    def _simulate_communication_investment(self, dates):
        """Simule l'investissement en communication"""
        base_investment = self.config["budget_base"] * 0.06
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2000:
                growth = 1 + 0.11 * max(0, (year - 2000)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_digital_investment(self, dates):
        """Simule l'investissement numérique"""
        base_investment = self.config["budget_base"] * 0.04
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:
                growth = 1 + 0.15 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.20)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_training_investment(self, dates):
        """Simule l'investissement en formation"""
        base_investment = self.config["budget_base"] * 0.03
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2005:
                growth = 1 + 0.08 * max(0, (year - 2005)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.14)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_international_investment(self, dates):
        """Simule l'investissement international"""
        base_investment = self.config["budget_base"] * 0.02
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:
                growth = 1 + 0.06 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.22)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _add_party_trends(self, df):
        """Ajoute des tendances réalistes pour le FN/RN"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Création du FN (1972)
            if year == 1972:
                df.loc[i, 'Revenus_Total'] *= 0.5  # Débuts très modestes
                df.loc[i, 'Adherents'] *= 0.8
            
            # Première présidentielle (1974)
            if year == 1974:
                df.loc[i, 'Depenses_Campagnes'] *= 3.0
                df.loc[i, 'Dons_Petits'] *= 2.5
            
            # Percée des européennes (1984)
            if year == 1984:
                df.loc[i, 'Financement_Public'] *= 2.0
                df.loc[i, 'Revenus_Total'] *= 1.4
            
            # Présidentielle 1988
            if year == 1988:
                df.loc[i, 'Depenses_Campagnes'] *= 2.8
                df.loc[i, 'Adherents'] *= 1.3
            
            # Affaire des fiches (1990)
            if year == 1990:
                df.loc[i, 'Depenses_Juridiques'] *= 2.2
            
            # Présidentielle 2002 (second tour)
            if year == 2002:
                df.loc[i, 'Revenus_Total'] *= 1.8
                df.loc[i, 'Dons_Petits'] *= 3.0
                df.loc[i, 'Adherents'] *= 1.6
            
            # Succession Marine Le Pen (2011)
            if year == 2011:
                df.loc[i, 'Investissement_Communication'] *= 1.5
                df.loc[i, 'Adherents'] *= 1.4
            
            # Prêts russes (2014)
            if year == 2014:
                df.loc[i, 'Emprunts'] *= 4.0
                df.loc[i, 'Aides_Etrangeres'] *= 3.5
            
            # Présidentielle 2017 (second tour)
            if year == 2017:
                df.loc[i, 'Depenses_Campagnes'] *= 3.2
                df.loc[i, 'Financement_Public'] *= 1.6
            
            # Changement de nom RN (2018)
            if year == 2018:
                df.loc[i, 'Investissement_Communication'] *= 1.8
                df.loc[i, 'Depenses_Communication'] *= 1.6
            
            # COVID-19 (2020)
            if year == 2020:
                df.loc[i, 'Revenus_Evenements'] *= 0.4
                df.loc[i, 'Investissement_Numérique'] *= 1.8
            
            # Élections 2022 (89 députés)
            if year == 2022:
                df.loc[i, 'Financement_Public'] *= 2.5
                df.loc[i, 'Revenus_Total'] *= 1.6
                df.loc[i, 'Elus_Nationaux'] = 89  # Réel chiffre 2022
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances du FN/RN"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des revenus et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des revenus
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Adhérents et scores électoraux
        ax4 = plt.subplot(4, 2, 4)
        self._plot_membership_electoral(df, ax4)
        
        # 5. Investissements stratégiques
        ax5 = plt.subplot(4, 2, 5)
        self._plot_strategic_investments(df, ax5)
        
        # 6. Indicateurs financiers spécifiques
        ax6 = plt.subplot(4, 2, 6)
        self._plot_specific_indicators(df, ax6)
        
        # 7. Évolution des élus
        ax7 = plt.subplot(4, 2, 7)
        self._plot_elected_officials(df, ax7)
        
        # 8. Situation financière et endettement
        ax8 = plt.subplot(4, 2, 8)
        self._plot_financial_situation(df, ax8)
        
        plt.suptitle(f'Analyse des Finances du {self.parti} ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'FN_RN_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des revenus et dépenses"""
        ax.plot(df['Annee'], df['Revenus_Total'], label='Revenus Totaux', 
               linewidth=2, color='#000080', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Total'], label='Dépenses Totales', 
               linewidth=2, color='#FF0000', alpha=0.8)
        
        ax.set_title('Évolution des Revenus et Dépenses (M€)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Ajouter des annotations pour les événements clés
        key_events = {
            1972: 'Création FN', 1974: '1ère présidentielle', 
            1984: 'Percée européenne', 2002: 'Second tour', 
            2011: 'Marine Le Pen', 2014: 'Prêts russes',
            2017: 'Second tour', 2018: 'RN', 2022: '89 députés'
        }
        
        for year, event in key_events.items():
            if year in df['Annee'].values:
                y_val = df[df['Annee'] == year]['Revenus_Total'].values[0]
                ax.annotate(event, (year, y_val), xytext=(10, 10), 
                           textcoords='offset points', fontsize=8, 
                           arrowprops=dict(arrowstyle='->', alpha=0.6))
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des revenus"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Cotisations_Adherents', 'Dons_Petits', 'Dons_Grands', 
                     'Financement_Public', 'Revenus_Evenements', 'Emprunts', 'Aides_Etrangeres']
        colors = ['#000080', '#FF0000', '#8B0000', '#000000', '#C0C0C0', '#800000', '#003366']
        labels = ['Cotisations', 'Dons Petits', 'Dons Grands', 'Financement Public', 
                 'Événements', 'Emprunts', 'Aides Étrangères']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Revenus (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Depenses_Personnel', 'Depenses_Campagnes', 'Depenses_Communication',
                     'Depenses_Juridiques', 'Depenses_Fonctionnement', 'Remboursements_Emprunts']
        colors = ['#000080', '#FF0000', '#8B0000', '#000000', '#C0C0C0', '#800000']
        labels = ['Personnel', 'Campagnes', 'Communication', 'Dépenses Juridiques', 'Fonctionnement', 'Remboursements']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_membership_electoral(self, df, ax):
        """Plot des adhérents et scores électoraux"""
        # Adhérents
        ax.bar(df['Annee'], df['Adherents']/1000, label='Adhérents (milliers)', 
              color='#000080', alpha=0.7)
        
        ax.set_title('Adhérents et Scores Présidentiels', fontsize=12, fontweight='bold')
        ax.set_ylabel('Adhérents (milliers)', color='#000080')
        ax.tick_params(axis='y', labelcolor='#000080')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Scores présidentiels en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Score_Presidentielles'], label='Score Présidentielles (%)', 
                linewidth=3, color='#FF0000')
        ax2.set_ylabel('Score Présidentielles (%)', color='#FF0000')
        ax2.tick_params(axis='y', labelcolor='#FF0000')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_strategic_investments(self, df, ax):
        """Plot des investissements stratégiques"""
        ax.plot(df['Annee'], df['Investissement_Communication'], label='Communication', 
               linewidth=2, color='#000080', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Numérique'], label='Numérique', 
               linewidth=2, color='#FF0000', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Formation'], label='Formation', 
               linewidth=2, color='#8B0000', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_International'], label='International', 
               linewidth=2, color='#000000', alpha=0.8)
        
        ax.set_title('Investissements Stratégiques (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_specific_indicators(self, df, ax):
        """Plot des indicateurs spécifiques au FN/RN"""
        # Taux d'exécution budgétaire
        ax.bar(df['Annee'], df['Taux_Execution_Budget']*100, label='Taux d\'Exécution (%)', 
              color='#000080', alpha=0.7)
        
        ax.set_title('Indicateurs Spécifiques FN/RN', fontsize=12, fontweight='bold')
        ax.set_ylabel('Taux d\'Exécution (%)', color='#000080')
        ax.tick_params(axis='y', labelcolor='#000080')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Dépenses juridiques en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Ratio_Depenses_Juridiques']*100, label='Dépenses Juridiques (% budget)', 
                linewidth=3, color='#FF0000')
        ax2.set_ylabel('Dépenses Juridiques (% budget)', color='#FF0000')
        ax2.tick_params(axis='y', labelcolor='#FF0000')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_elected_officials(self, df, ax):
        """Plot de l'évolution des élus"""
        ax.plot(df['Annee'], df['Elus_Locaux']/100, label='Élus Locaux (centaines)', 
               linewidth=2, color='#000080', alpha=0.8)
        
        ax.set_title('Évolution des Élus', fontsize=12, fontweight='bold')
        ax.set_ylabel('Élus Locaux (centaines)', color='#000080')
        ax.tick_params(axis='y', labelcolor='#000080')
        ax.grid(True, alpha=0.3)
        
        # Élus nationaux en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Elus_Nationaux'], label='Élus Nationaux', 
                linewidth=2, color='#FF0000', alpha=0.8)
        ax2.set_ylabel('Élus Nationaux', color='#FF0000')
        ax2.tick_params(axis='y', labelcolor='#FF0000')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_financial_situation(self, df, ax):
        """Plot de la situation financière"""
        # Solde financier
        ax.bar(df['Annee'], df['Solde_Financier']*100, label='Solde Financier (% du budget)', 
              color=df['Solde_Financier'].apply(lambda x: '#000080' if x > 0 else '#FF0000'), alpha=0.7)
        
        ax.set_title('Situation Financière et Endettement', fontsize=12, fontweight='bold')
        ax.set_ylabel('Solde Financier (% du budget)', color='#000080')
        ax.tick_params(axis='y', labelcolor='#000080')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Endettement en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Endettement'], label='Endettement (M€)', 
                linewidth=3, color='#8B0000')
        ax2.set_ylabel('Endettement (M€)', color='#8B0000')
        ax2.tick_params(axis='y', labelcolor='#8B0000')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques pour le FN/RN"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - {self.parti} ({self.start_year}-{self.end_year})")
        print("=" * 70)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Revenus_Total'].mean()
        avg_expenses = df['Depenses_Total'].mean()
        avg_adherents = df['Adherents'].mean()
        avg_execution = df['Taux_Execution_Budget'].mean() * 100
        
        print(f"Revenus moyens annuels: {avg_revenue:.2f} M€")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M€")
        print(f"Adhérents moyens: {avg_adherents:,.0f} personnes")
        print(f"Taux d'exécution budgétaire moyen: {avg_execution:.1f}%")
        
        # 2. Croissance historique
        print("\n2. 📊 ÉVOLUTION HISTORIQUE:")
        revenue_growth = ((df['Revenus_Total'].iloc[-1] / 
                          df['Revenus_Total'].iloc[0]) - 1) * 100
        adherents_growth = ((df['Adherents'].iloc[-1] / 
                           df['Adherents'].iloc[0]) - 1) * 100
        
        print(f"Évolution des revenus ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Évolution des adhérents ({self.start_year}-{self.end_year}): {adherents_growth:.1f}%")
        
        # 3. Structure financière spécifique
        print("\n3. 📋 STRUCTURE FINANCIÈRE SPÉCIFIQUE:")
        small_donations_share = (df['Dons_Petits'].mean() / df['Revenus_Total'].mean()) * 100
        legal_share = (df['Depenses_Juridiques'].mean() / df['Depenses_Total'].mean()) * 100
        debt_share = (df['Endettement'].mean() / df['Revenus_Total'].mean()) * 100
        
        print(f"Part des petits dons dans les revenus: {small_donations_share:.1f}%")
        print(f"Part des dépenses juridiques: {legal_share:.1f}%")
        print(f"Endettement moyen vs revenus: {debt_share:.1f}%")
        
        # 4. Performance et difficultés
        print("\n4. 🎯 PERFORMANCE ET DIFFICULTÉS:")
        avg_balance = df['Solde_Financier'].mean() * 100
        last_debt = df['Endettement'].iloc[-1]
        max_score = df['Score_Presidentielles'].max()
        
        print(f"Solde financier moyen: {avg_balance:.1f}% du budget")
        print(f"Endettement final: {last_debt:.1f} M€")
        print(f"Meilleur score présidentiel: {max_score:.1f}%")
        
        # 5. Spécificités du FN/RN
        print(f"\n5. 🌟 SPÉCIFICITÉS DU FN/RN:")
        print(f"Orientation politique: {self.config['orientation']}")
        print(f"Électorat cible: {', '.join(self.config['electorat_cible'])}")
        print(f"Spécificités: {', '.join(self.config['specificites'])}")
        
        # 6. Événements marquants
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 1972: Création du Front National")
        print("• 1974: Première candidature présidentielle de Jean-Marie Le Pen")
        print("• 1984: Percée aux élections européennes")
        print("• 2002: Jean-Marie Le Pen au second tour de la présidentielle")
        print("• 2011: Marine Le Pen prend la tête du parti")
        print("• 2014: Controverse des prêts russes")
        print("• 2017: Marine Le Pen au second tour de la présidentielle")
        print("• 2018: Changement de nom - Rassemblement National")
        print("• 2022: Obtention de 89 députés à l'Assemblée nationale")
        
        # 7. Recommandations stratégiques
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        print("• Poursuivre la professionnalisation de la gestion financière")
        print("• Diversifier les sources de financement")
        print("• Renforcer la collecte des cotisations")
        print("• Optimiser l'utilisation du financement public")
        print("• Maîtriser les dépenses juridiques")
        print("• Réduire la dépendance aux emprunts")
        print("• Développer le fundraising numérique")
        print("• Renforcer la transparence financière")

def main():
    """Fonction principale pour l'analyse du FN/RN"""
    print("🏛️ ANALYSE DES FINANCES DU FRONT NATIONAL/RASSEMBLEMENT NATIONAL (1972-2025)")
    print("=" * 70)
    
    # Initialiser l'analyseur
    analyzer = FN_RN_FinanceAnalyzer()
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = 'FN_RN_financial_data_1972_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Adherents', 'Revenus_Total', 'Depenses_Total', 'Score_Presidentielles']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des finances du {analyzer.parti} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Revenus, dépenses, adhérents, élus, scores électoraux")

if __name__ == "__main__":
    main()