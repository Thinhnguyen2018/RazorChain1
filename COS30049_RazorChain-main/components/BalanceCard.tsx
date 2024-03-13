/**
 * Update: Responsive!
 * This is a component to use in /pages/profile/[walletAddress]
 * It is a card showing token symbol and wallet balance
 */
import React, { useState, useEffect } from 'react';
import { Card, Spinner, Stack, Text } from '@chakra-ui/react';
import axios from 'axios';
import { useAddress } from '@thirdweb-dev/react';

// Must get tokenAddress to get verifiedTokensList
type Props = {
    symbol: string;
    balance: number;
};

export default function BalanceCard({ symbol, balance }: Props) {
    // Get current user's address
    const address = useAddress();
    const [RZCtoken, setRZCtoken] = useState('');
    const [RZCsupply, setRZCsupply] = useState('');
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchTokenSymbol = async () => {
            setLoading(true);
            try {
                const response = await axios.get('http://localhost:8000/assets');
                // Adjust the index as needed to match your actual data structure
                setRZCtoken(response.data.content.data[5].asset_symbol);
            } catch (error) {
                console.error('Error fetching data:', error);
                setRZCtoken('Error');
            } finally {
                setLoading(false);
            }
        };

        fetchTokenSymbol();
    }, []);

    useEffect(() => {
        const fetchTokenSymbol2 = async () => {
            setLoading(true);
            try {
                const response = await axios.get('http://localhost:8000/assets');
                // Adjust the index as needed to match your actual data structure
                setRZCsupply(response.data.content.data[5].total_supply);
            } catch (error) {
                console.error('Error fetching data:', error);
                setRZCsupply('Error');
            } finally {
                setLoading(false);
            }
        };

        fetchTokenSymbol2();
    }, []);

    return (
        <Card p={4} width={"100%"} height={"100%"} border={"2px solid"} borderColor={"gray.100"}>
            {/**
             * Check if contract meta is loading, display the stack after done
             * Show the symbol of token
             * Show the wallet balance after loading tokenbalance
             */}
            <Stack textAlign={"center"}>
                <Text fontWeight={"bold"} fontSize={"2xl"}>{RZCtoken}</Text>
                <Text>Balance:</Text>
                <Text fontSize={"3xl"} fontWeight={"bold"}>{RZCsupply}</Text>
            </Stack>
        </Card>
    )
}