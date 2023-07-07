SELECT cl.nome AS cliente_nome, ROUND(SUM((t.valor_total - (t.valor_total * COALESCE(t.percentual_desconto, 0) / 100)) * ct.percentual / 100), 2) AS valor
FROM cliente cl
INNER JOIN contrato ct ON ct.cliente_id = cl.cliente_id
INNER JOIN transacao t ON t.contrato_id = ct.contrato_id
WHERE ct.ativo = 1
GROUP BY cl.nome;
