from app.performance.ranking_engine import rank_salespersons


def get_performance_dashboard(db, salesperson_ids):
    ranking = rank_salespersons(db, salesperson_ids)

    return {
        "ranking": ranking,
        "top_salesperson": ranking[0] if ranking else None
    }
