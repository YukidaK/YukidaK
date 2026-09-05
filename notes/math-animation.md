# Butterfly Curve

A animação exibida no meu perfil do GitHub é gerada matematicamente utilizando
uma curva paramétrica conhecida como **Butterfly Curve**.

## Fórmula

A curva é definida por:

\[
x(t) =
\sin(t)
\left(
e^{\cos(t)}
- 2\cos(4t)
- \sin^5\left(\frac{t}{12}\right)
\right)
\]

\[
y(t) =
\cos(t)
\left(
e^{\cos(t)}
- 2\cos(4t)
- \sin^5\left(\frac{t}{12}\right)
\right)
\]

com:

\[
0 \leq t \leq 12\pi
\]

## Como a animação funciona

O script calcula milhares de pontos da curva antes de iniciar a animação.

Em cada frame, uma quantidade maior desses pontos é exibida, criando a impressão
de que a função está sendo desenhada progressivamente no plano.

A animação é gerada utilizando:

- Python
- NumPy
- Matplotlib
- Pillow

## Gerando novamente

A partir da raiz do repositório:

```bash
python scripts/generate_animation.py