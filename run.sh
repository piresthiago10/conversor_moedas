#!/usr/bin/env bash
sudo docker-compose up -d --build 
cd conversor_front
sudo docker-compose -f docker-compose-front.yml up -d --build