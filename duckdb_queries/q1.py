import duckdb

from duckdb_queries import utils

Q_NUM = 1


def q():
    lineitem = utils.get_line_item_ds()

    query_str = f"""
    select
        l_returnflag,
        l_linestatus,
        sum(l_quantity) as sum_qty,
        sum(l_extendedprice) as sum_base_price,
        sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
        sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
        avg(l_quantity) as avg_qty,
        avg(l_extendedprice) as avg_price,
        avg(l_discount) as avg_disc,
        count(*) as count_order
    from
        {lineitem}
    where
        l_shipdate <= '1998-09-02'
    group by
        l_returnflag,
        l_linestatus
    order by
        l_returnflag,
        l_linestatus
    """

    q_final = duckdb.sql(query_str)

    utils.run_query(Q_NUM, q_final)


if __name__ == "__main__":
    q()
