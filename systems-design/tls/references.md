# TLS

ByteByteGo SSL, TLS, HTTPS Explained
https://www.youtube.com/watch?v=j9QmMEWmcfo

## TLS - Transport Layer Security

1. TCP handshake. Browser starts TCP connection with server.

```
> TCP SYN
< TCP SYN + ACK
> TCP ACK
-- Connection established
-- ASYMmetric encryption of keys
```

2. Certificate Check

```
> Client Hello (TLS version 1.3, Cypher suite)
< Server Hello (Selected TLS, Selected cypher suite)
< Certificate
< Server Hello Done
```

3. Key Exchange

```
> Client Key Exchange
> Change Cipher Spec
> Finished
< Change cipher spec
< Finished
```

The client has a session key, which it uses the server PUBLIC KEY to encrypt. The server decrypts the session key using its PRIVATE KEY.

4. Data Transmission

```
> Encrypted data
-- session key used for SYMMETRIC encryption in RSA --
< Encrypted data
```

## TLS 1.3

F Helminth uses large prime numbers for shared session key, and no public key is transmitted.
